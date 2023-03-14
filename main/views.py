from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator 
from django.template import RequestContext
from django.db.models import Avg,Count
from django.contrib import messages
from product.models import Product
from vendor.models import *
from cart.models import *
from .manager import *
from .models import *
from .forms import *
import uuid

# Create your views here.

def home(request):
	products = Product.objects.all().order_by('-id')
	grocery = Product.objects.filter(category_id = 1).order_by('-id')
	health = Product.objects.filter(category_id = 2).order_by('-id')
	beauty = Product.objects.filter(category_id = 3).order_by('-id')
	accessory= Product.objects.filter(category_id = 4).order_by('-id')
	electronic= Product.objects.filter(category_id = 5).order_by('-id')
	fashion = Product.objects.filter(category_id = 6).order_by('-id')
	stationery = Product.objects.filter(category_id = 7).order_by('-id')

	return render(request,'home.html', 
		{'products':products,'grocery':grocery,'health':health,'beauty':beauty,
		'accessory':accessory,'electronic':electronic,'fashion':fashion,'stationery':stationery})

def search(request):
	prods=Product.objects.all().order_by('name')[:8]
	searched = request.GET.get('q')
	if searched == None:
		products=[]
	else:
		products=Product.objects.all().filter(name__icontains=searched).order_by('name')	
	return render(request, 'search.html', {'products':products, 'searched':searched,'prods':prods})

def shop(request):
	products = Product.objects.all().order_by('name')

	paginator=Paginator(products, 30)
	page_num=request.GET.get('page',1)
	products=paginator.page(page_num)

	return render(request, 'shop.html', {'products':products})

def category_product_list(request,cat_id,title):
	page = 'category-product-list'
	category=Category.objects.get(id=cat_id)
	products=Product.objects.filter(category=category).order_by('-id')
	cats=Category.objects.all().exclude(id=cat_id)

	paginator=Paginator(products,30)
	page_num=request.GET.get('page',1)
	products=paginator.page(page_num)
	
	return render(request, 'category.html',
		{'products':products,'cats':cats,'category':category,})		

def registerUser(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method=='POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		if password1 != password2:
			messages.error(request, f"Oops! Your passwords does not match!.")
		if User.objects.filter(username = username).exists():
			messages.error(request, f"Oops! User with username exists!.")
		if User.objects.filter(email = email).exists():
			messages.error(request, f"Oops! User with email exists!.")	
			
		form=SignupForm(request.POST)
		if form.is_valid():
			form.save()
			new_user(username, email)			
			username=form.cleaned_data.get('username')
			pwd=form.cleaned_data.get('password1')
			user=authenticate(username=username,password=pwd)
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('home')

	form=SignupForm
	return render(request, 'registration/register.html',{'form':form})

def loginView(request):
    # restrict login page for logged in user 
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_url = request.GET.get('next','home')
                return redirect(redirect_url)
            else:
                messages.error(request, f"Oops! Username or Password is invalid. Please try again.")
                
        return render(request, 'registration/login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')  

def contact(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		contact = Contact.objects.create(email=email, phone=phone, message=message)
		if contact:
			messages.success(request, f"Your message have been sent! Thank you for contacting us ")

	return render(request, 'footer/contact.html', {})

def about_us(request):
	reviews = ExcelcartReview.objects.all() 
	return render(request, 'footer/about.html', {'reviews':reviews})	

def faq(request):
	faqs = Faq.objects.all()
	return render(request, 'footer/faq.html', {'faqs':faqs})			

@login_required
def user_dash(request):
	orders = CartOrder.objects.filter(user = request.user).order_by('-id')
	false_ord = CartOrder.objects.filter(user = request.user, paid_status = False)
	address = CustomerAddress.objects.filter(user = request.user)
	wishlist = Wishlist.objects.filter(user=request.user).order_by('-id')[:10]
	is_vendor = Vendor.objects.filter(user=request.user)

	if 'delete-wish' in request.POST:
		pid= request.POST.get('delID')
		product = Wishlist.objects.get(pk= pid)
		product.delete()
		return redirect('/accounts/dashboard')

	if 'addform' in request.POST:
		city = request.POST.get('city')
		address = request.POST.get('address')
		phone = request.POST.get('phone')
		place = request.POST.get('place')
		if CustomerAddress.objects.filter(user=request.user, city=city, address=address, phone=phone, name=place).exists():
			return redirect('/accounts/dashboard')
		else:
			CustomerAddress.objects.create(user=request.user, city=city, address=address, phone=phone, name=place)
			return redirect('/accounts/dashboard')

	if 'add_edit' in request.POST:
		city = request.POST.get('city')
		address = request.POST.get('address')
		phone = request.POST.get('phone')
		place = request.POST.get('place')
		add_id = request.POST.get('addid')

		edit_add = CustomerAddress.objects.get(pk = add_id)
		edit_add.city =  city
		edit_add.address = address
		edit_add.phone = phone
		edit_add.name = place
		edit_add.save()
		return redirect('/accounts/dashboard')
	
	if 'add_delete' in request.POST:
		add_id = request.POST.get('delete_addid')	
		delete_add= CustomerAddress.objects.get(pk=add_id)
		delete_add.delete()
		return redirect('/accounts/dashboard')

	if 'edit_profile' in request.POST:	
		username = request.POST.get('username')
		email = request.POST.get('email')
		
		user= User.objects.get(id = request.user.id)
		user.username = username
		user.email=email
		user.save()
		return redirect('/accounts/dashboard')
			

	return render(request, 'registration/user_dashboard.html', 
		{'orders':orders, 'false_ord':false_ord, 'address':address,'wishlist':wishlist,'is_vendor':is_vendor,
		})

@login_required
def order_tracking(request):

	if request.method == 'POST':
		orderCode = request.POST.get('order-code')
		order = CartOrder.objects.filter(user = request.user, code=orderCode)
		if order:
			Tracking.objects.create(user=request.user,Ordercode=orderCode)
			return render(request, 'order-tracked.html', {'order':order})
		else:
			messages.error(request, f"Oops! Username or orderID is invalid. Please try again.")
	
	return render(request, 'order-tracking.html', {})


def forgot_password(request):	

	if request.method=='POST':

		email = request.POST.get('email')	

		if not User.objects.filter(email = email):
			messages.error(request, 'No user found with this email')
			return redirect('forgot-password')

		token = str(uuid.uuid4())
		user = User.objects.get(email = email)
		user_obj= user.email
		username = user.username			

		forget_password_email(username,user_obj, token)
		UserToken.objects.create(user =user, token=token)
		messages.error(request, 'Check your email to set up new password.')		
		return redirect('forgot-password')

	return render(request, 'registration/forgot-password.html',{})

def reset_password(request, token):
	tokenuser = UserToken.objects.filter(token = token)	

	if tokenuser:
		for usert in tokenuser:
			user_id = usert.user.id	

	else:
		messages.error(request, "Enter email to get a link")
		return redirect('forgot-password')	

	if request.method == 'POST':
		new_password = request.POST.get('password1')
		confirm_password = request.POST.get('password2')

		if new_password != confirm_password:
			messages.error(request, "Passwords must be the same!")
			return redirect(f'/accounts/reset-password/{token}/')			

		user= User.objects.get(id = user_id)
		user.set_password(new_password)
		user.save()

		change_password_success(user.username, user.email)
		return redirect('login')			

	return render(request, 'registration/change-password.html', {})

def change_password(request):
	if request.method == 'POST':
		new_password = request.POST.get('password1')
		confirm_password = request.POST.get('password2')

		if new_password != confirm_password:
			messages.error(request, "Passwords must be the same!")
			return redirect(f'change-password')			

		user= User.objects.get(id = request.user.id)
		user.set_password(new_password)
		user.save()
		messages.success(request, "Your password have been changed. Login to continue")
		return redirect('login')

	return render(request, 'registration/change-password.html', {})	



def handler404(request, exception):
    return render(request, '404.html', status=404)



