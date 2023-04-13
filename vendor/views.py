from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Avg,Count
from django.contrib import messages
from django.utils import timezone
from product.models import *
from main.manager import *
from cart.models import *
from .models import *
from .forms import *
import uuid

# Create your views here.

def become_seller(request):
	vendors = Vendor.objects.all()
	return render(request, 'become-seller.html', {'vendors':vendors})

@login_required
def seller_reg(request):
	vend = Vendor.objects.filter(user=request.user)
	if vend:
		return redirect('/vendor/dashboard')

	else:	
		if Vendor.objects.all().count() == 52:
			messages.error(request,'Contact the Admin to start selling on Execlecart')
			return redirect('contact')

		elif request.method == 'POST':
			vendorname = request.POST.get('vendorname')
			vendorimage = request.FILES['vendorimage']
			vendordesc = request.POST.get('vendordesc')
			vendoradd = request.POST.get('vendoradd')
			vendorcontact = request.POST.get('vendorcontact')
			vendormail = request.POST.get('vendormail')
			accept = request.POST.get('accept')

			if vendordesc == '':
				messages.error(request,'Description Field Cannot Be Empty!')
				return redirect('seller-form')		

			elif vendoradd == '':
				messages.error(request,'Address Field Cannot Be Empty!')
				return redirect('seller-form')	

			elif vendorcontact == '':
				messages.error(request,'Phone Contact Field Cannot Be Empty!')
				return redirect('seller-form')	

			elif vendormail == '':
				messages.error(request,'Business Email Field Cannot Be Empty!')
				return redirect('seller-form')	

			elif Vendor.objects.filter(name=vendorname).exists():
				messages.error(request, f"Vendor name already choosen!")
				return redirect('/vendor/register')	

			else:
				vendor= Vendor.objects.create(
						user= request.user,
						name= vendorname,
						image= vendorimage,
						description= vendordesc,
						address= vendoradd,
						phone= vendorcontact,
						email= vendormail,
						)

				#token = str(uuid.uuid4())
				#new_vendor(vendor, token)
				#VendorToken.objects.create(vendor =vendor, token=token)
				return redirect('/vendor/dashboard')

	return render(request, 'seller-form.html', {})

def vendor_list(request):
	vendors = Vendor.objects.filter(approve=True).order_by('-name')

	paginator=Paginator(vendors,30)
	page_num=request.GET.get('page',1)
	vendors=paginator.page(page_num)
	return render(request, 'vendor-list.html', {'vendors':vendors})

def confirm_email(request, token):
	vend = VendorToken.objects.get(token = token)
	if vend:
		vendor = Vendor.objects.get(id=vend.vendor.id)
		vendor.approve = False
		vendor.save()
		return redirect('vendor-dashboard')
	else:
		Vendor.objects.filter(user=request.user).delete()
		messages.success(request, "Please enter a valid email!")
		return redirect('seller-form')	

def vendor_detail(request, name):
	vendor = Vendor.objects.get(name = name)
	products = Product.objects.filter(vendor= vendor)

	if VendorReview.objects.filter(vendor=vendor).count() > 0:
		vendor.avg_ratings  = VendorReview.objects.filter(vendor=vendor).aggregate(Avg('rating'))['rating__avg']
		vendor.save()
	return render(request, 'vendor-detail.html', {'vendor':vendor, 'products':products})	

@login_required
def vendor_dashboard(request):
	vendor = Vendor.objects.filter(user=request.user)
	if vendor:
		vend_approve = Vendor.objects.filter(user=request.user, approve = True)

		for v in vendor:
			ven = v.name
			venid = v.id
		vend_sale = CartOrderItems.objects.filter(vendor=ven)	
		ord_pending = CartOrderItems.objects.filter(order__order_status='process', vendor=ven)	
		popular_prod= Product.objects.filter(vendor__name=ven).order_by('-sales')[:6]
		order_items = CartOrderItems.objects.filter(vendor=ven).order_by('-id')

		payments = VendorPayment.objects.filter(vendor = v)

		payouts = VendorPayout.objects.filter(vendor=v)

		products = Product.objects.filter(vendor__name=ven).order_by('-id')

		if 'pay_add' in request.POST:
			bank = request.POST.get('bankname')
			acctno = request.POST.get('acctno')
			acctname = request.POST.get('acctname')
			VendorPayment.objects.create(vendor = v, bank=bank, acct_no=acctno, acct_name=acctname)

		if 'pay_edit' in request.POST:	
			pay_id = request.POST.get('edit_payid')
			bank = request.POST.get('edit_bankname')
			acctno = request.POST.get('edit_acctno')
			acctname = request.POST.get('edit_acctname')

			edit_vendorpay = VendorPayment.objects.get(pk = pay_id, vendor = v)
			edit_vendorpay.bank = bank
			edit_vendorpay.acct_no = acctno
			edit_vendorpay.acct_name = acctname
			edit_vendorpay.save()

		if 'pay_delete' in request.POST:
			pay_id = request.POST.get('delete_payid')
			delete_vendorpay = VendorPayment.objects.get(pk=pay_id, vendor=v)
			delete_vendorpay.delete()			

		if 'profile_edit' in request.POST:
			vend_name = request.POST.get('vend_name')
			vend_email = request.POST.get('vend_email')
			vend_phone = request.POST.get('vend_phone')
			vend_desc = request.POST.get('vend_desc')
			vend_add = request.POST.get('vend_add')

			vend_edit = Vendor.objects.get(name = v.name)
			vend_edit.name = vend_name
			vend_edit.email = vend_email
			vend_edit.phone = vend_phone
			vend_edit.descriptionri = vend_desc	
			vend_edit.address = vend_add	
			vend_edit.save()
			messages.success(request, "Profile Successfully Changed!")
			return redirect('vendor-dashboard')

		if 'vend_image' in request.POST:
			vend_img = request.FILES.get('vendor_image')
			vend_img_edit = Vendor.objects.get(name = v.name)
			if vend_img == None:
				vend_img_edit.image = vend_img_edit.image
			else:		
				vend_img_edit.image = vend_img
			vend_img_edit.save()
			return redirect('/vendor/dashboard')

		if 'product_edit' in request.POST:
			pid = request.POST.get('pid')
			pname = request.POST.get('pname')
			pimage = request.FILES.get('pimage')
			psize = request.POST.get('psize')
			pprice = request.POST.get('pprice')
			pdisprice = request.POST.get('pdisprice')
			pnumber = request.POST.get('pnumber')

			p_edit = Product.objects.get(pk=pid)
			var_edit = Variation.objects.get(product=p_edit, size=psize)

			if pprice == '0':
				var_edit.price = var_edit.price
			else:	
				var_edit.price = pprice

			if pdisprice == '0':
				var_edit.dis_price = var_edit.dis_price
			else:	
				var_edit.dis_price = pdisprice

			if pnumber == '0':
				p_edit.number = p_edit.number
			else:					
				p_edit.number = pnumber

			p_edit.name = pname
			if pimage == None:
				p_edit.thumb_nail = p_edit.thumb_nail
			else:	
				p_edit.thumb_nail = pimage
			var_edit

			p_edit.save()
			var_edit.save()
			messages.success(request, "Product Edit Saved!")	

		if 'var_add' in request.POST:
			p_id = request.POST.get('pid')	
			prod = Product.objects.get(pk=p_id)

			add_var = VariationForm(request.POST)
			if add_var.is_valid:
				var_save = add_var.save(commit=False)
				var_save.product = prod	 
				
				var_save.save()
				if Variation.objects.filter(product=prod, size=var_save.size).count() > 1:
					Variation.objects.get(pk = var_save.id,product=prod, size=var_save.size).delete()

		varform = VariationForm()	

		if 'prod_delete' in request.POST:
			pid = request.POST.get('pid')
			delete_prod = Product.objects.get(pk=pid)
			delete_prod.delete()	

		if 'payout' in request.POST:
			wallet = VendorWallet.objects.get(vendor=v)
			withdrawal_amount = float(request.POST.get('withdrawal_amount'))
			bank_choice = request.POST.get('bank')
			bank = VendorPayment.objects.get(id = bank_choice)

			if wallet.balance >= withdrawal_amount:

				current_time = timezone.now()

				if wallet.last_withdrawal_time is None or (current_time - wallet.last_withdrawal_time).days >= 3:
					wallet.balance = int(wallet.balance) - int(withdrawal_amount)
					wallet.last_withdrawal_time = current_time
					wallet.save()
					VendorPayout.objects.create(vendor =v, amount=withdrawal_amount, bank=bank)
					messages.success(request, 'Withdrawal request submitted successfully.')
				else:
					messages.error(request, 'You can only withdraw after 3 days interval.')
			else:
				messages.error(request, 'Insufficient balance for withdrawal.')	

	else:
		return redirect('user-dashboard')	

	return render(request, 'vendor-dashboard.html', 
		{'vendor':vendor,'vend_sale':vend_sale,'ord_pending':ord_pending,'popular_prod':popular_prod,
		 'order_items':order_items,'products':products,'payments':payments,'v':v,
		 'varform':varform,'vend_approve':vend_approve, 'payouts':payouts

		})	

@login_required
def add_product(request):
	vend = Vendor.objects.filter(user=request.user)	

	if vend:

		vendor = get_object_or_404(Vendor, user = request.user)
		cat = Category.objects.get(pk=1)

		if request.method == 'POST':

			productform = ProductForm(request.POST, request.FILES)
			variationform = VariationForm(request.POST)
			prodinfoform = ProductInfoForm(request.POST)

			files = request.FILES.getlist('files')

			if productform.is_valid():
				product = productform.save(commit=False)
				product.vendor = vendor	
				product.category = cat
				product.save()		

				for i in files:
					ProductImage.objects.create(product = product, image=i)

				if variationform.is_valid():
					prod_var = variationform.save(commit=False)
					prod_var.product = product
					prod_var.save()

				if prodinfoform.is_valid():
					prod_info = prodinfoform.save(commit=False)
					prod_info.product = product
					prod_info.save()

				messages.success(request, "New Product Added Successfully")
				return redirect('/vendor/dashboard')		

			else:
				messages.error(request, f"Oops! Something went wrong. Make sure you fill the forms with the appropriate info.")				

		else:
			productform = ProductForm()	
			variationform = VariationForm()	
			prodinfoform = ProductInfoForm()
	else:
		return redirect('shop')		
		
	return render(request, 'add-product.html', {
		'pform':productform,'variationform':variationform,'prodinfoform':prodinfoform,
		})	

