from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import *
from paystackpay.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from main.forms import *


# Create your views here.

# Add to cart
def add_to_cart(request):
	cart_p={}
	cart_p[str(request.GET.get('id'))]={
		'img':request.GET.get('img'),
		'title':request.GET.get('title'),
		'color':request.GET.get('color'),
		'size':request.GET.get('size'),
		'qty':request.GET.get('qty'),
		'price':request.GET.get('price'),
		'cat':request.GET.get('cat'),
		'vendor':request.GET.get('vendor')		
	}
	if 'cartdata' in request.session:
		if str(request.GET.get('id')) in request.session['cartdata']:
			cart_data=request.session['cartdata']
			cart_data[str(request.GET.get('id'))]['qty']=int(cart_p[str(request.GET.get('id'))]['qty'])
			cart_data.update(cart_data)
			request.session['cartdata']=cart_data
		else:
			cart_data=request.session['cartdata']
			cart_data.update(cart_p)
			request.session['cartdata']=cart_data
	else:
		request.session['cartdata']=cart_p
	return JsonResponse({'data':request.session['cartdata'],'totalitems':len(request.session['cartdata'])})

def cart_list(request):
	total_amt=0
	total=0
	delivery=0
	if 'cartdata' in request.session:
		for p_id,item in request.session['cartdata'].items():
			total_amt+=int(item['qty'])*int(item['price'])

			if total_amt > 5000:
				delivery = total_amt * 11/100
			else:
				delivery = 500

			total = total_amt + delivery		
		return render(request, 'cart.html',
			{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,'delivery':delivery,'total':total})
	else:
		return render(request, 'cart.html',{'cart_data':'','totalitems':0,'total_amt':total_amt})	

def delete_cart_item(request):
	total_amt=0	
	discount=0
	total=0
	delivery=0
	p_id=str(request.GET.get('id'))
	if 'cartdata' in request.session:
		if p_id in request.session['cartdata']:
			cart_data=request.session['cartdata']
			del request.session['cartdata'][p_id]
			request.session['cartdata']=cart_data
	total_amt=0
	for p_id,item in request.session['cartdata'].items():
		total_amt+=int(item['qty'])*int(item['price'])
		if total_amt > 5000:
			delivery = total_amt * 11/100
		else:
			delivery = 500

		total = total_amt + delivery
	t=render_to_string('ajax/cart-list.html',
		{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,'discount':discount,'delivery':delivery,'total':total})
	return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})

# Delete Cart Item
def update_cart_item(request):
	total_amt=0	
	discount=0
	total=0
	p_id=str(request.GET['id'])
	p_qty=request.GET.get('qty')
	p_size = request.GET.get('size')
	p_price = request.GET.get('price')
	if 'cartdata' in request.session:
		if p_id in request.session['cartdata']:
			cart_data=request.session['cartdata']
			cart_data[str(request.GET['id'])]['qty']= p_qty
			cart_data[str(request.GET['id'])]['size']= p_size
			cart_data[str(request.GET['id'])]['price']= p_price
			request.session['cartdata']=cart_data			
	for p_id,item in request.session['cartdata'].items():
		total_amt+=int(item['qty'])*int(item['price'])
		if total_amt > 5000:
			delivery = total_amt * 11/100
		else:
			delivery = 500

		total = total_amt + delivery
	t=render_to_string('ajax/cart-list.html',
		{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,'discount':discount,'delivery':delivery,'total':total})
	return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})

def add_wishlist(request):
	pid=request.GET['product']
	product=Product.objects.get(pk=pid)
	data={}
	checkw=Wishlist.objects.filter(product=product,user=request.user).count()
	if checkw > 0:
		data={
			'bool':False
		}
	else:
		wishlist=Wishlist.objects.create(
			product=product,
			user=request.user
		)
		data={
			'bool':True
		}
	return JsonResponse(data)

@login_required
def wishlist(request):
	wlist=Wishlist.objects.filter(user=request.user).order_by('-id')
	if request.method == 'POST':
		pid= request.POST.get('delID')
		product = Wishlist.objects.get(pk= pid)
		product.delete()
	return render(request, 'wishlist.html',{'wlist':wlist})


@login_required
def checkout(request):	
	total_amt=0
	totalAmt = 0
	discount=0
	total=0 
	delivery=0

	address= CustomerAddress.objects.filter(user = request.user)
	if 'cartdata' in request.session:
		for p_id,item in request.session['cartdata'].items():
			totalAmt+=int(item['qty'])*int(item['price'])

			order=CartOrder.objects.create(
					user=request.user,
					total_amt=totalAmt
				)

		for p_id,item in request.session['cartdata'].items():
			total_amt+=int(item['qty'])*float(item['price'])
			items=CartOrderItems.objects.create(
					order=order,
					invoice_no='INV-'+str(order.id),
					item=item['title'],
					image=item['img'],
					qty=item['qty'],
					price=item['price'],
					total=float(item['qty'])*float(item['price']),
					size= item['size'],
					color= item['color'],
					vendor= item['vendor'],
					)			

			if total_amt > 5000:
				delivery = total_amt * 11/100
			else:
				delivery = 500

			total = total_amt + delivery	

		formadd = AddressForm()	
		if 'addform' in request.POST:
			formadd = AddressForm(request.POST)
			if formadd.is_valid:
				add_form= formadd.save(commit=False)
				add_form.user = request.user
				add_form.save()
			else:
				messages.error(request, "Add correct address details!")	

		if 'order' in request.POST:
			customer = request.user.username
			address = request.POST.get('address')
			email = request.user.email
			payment_choice = request.POST.get('payment')
			amount = total
			note = request.POST.get('note')	
			code = request.POST.get('code')	
			time = request.POST.get('time')	
			date = request.POST.get('date')				

			coupon = CouponCode.objects.filter(code = code)
			if coupon:
				for c in coupon:
					discount = int(c.per_off) * total_amt/100
			else:
				discount=0
				messages.error(request, f"Oops! Coupon code is invalid.")
		
			total = total_amt + delivery - discount	

			payment = Payment.objects.create(
				order_note=note, email=email, customer=customer, address_id=address, discount=discount, amount=total, payment_option=payment_choice
				)
			p = get_object_or_404(Product, name=item['title'])
			p.sales = p.sales+1
			p.save()

			sales_num = Product.objects.filter(name=item['title'])
			for prod in sales_num:
				prod.number = prod.number-1
				prod.save()

			if payment_choice == 'Cash':

				return render(request, 'by_cash.html',
					{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,
					 'payment':payment,'delivery':delivery,'discount':discount,'total':total,'address':address})

			elif payment_choice == 'Transfer':

				return render(request, 'by_transfer.html',
					{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,
					 'payment':payment,'delivery':delivery,'discount':discount,'total':total,'address':address})

			elif payment_choice == 'Paystack':

				return render(request, 'by_paystack.html',
					{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,
					 'payment':payment,'delivery':delivery,'discount':discount,'total':total,'address':address, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
						 		 	
		return render(request, 'checkout.html',
			{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,'delivery':delivery,
			'discount':discount,'total':total,'address':address,'formadd':formadd})
		
	else:
		return render(request, 'checkout.html',
			{'cart_data':'','totalitems':0,'total_amt':total_amt,'discount':discount,'address':address, 'formadd':formadd})