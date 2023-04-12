from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import *
from main.models import *
from paystackpay.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from main.forms import *
from main.manager import *


# Create your views here.

# Add to cart
def add_to_cart(request):
	if request.GET.get('size') == '':
		p = Variation.objects.get(product__ref = request.GET.get('ref'))
		price = p.price
		size= p.size
	else:
		price = request.GET.get('price')
		size = request.GET.get('size') 
		
	cart_p={}
	cart_p[str(request.GET.get('id'))]={
		'img':request.GET.get('img'),
		'title':request.GET.get('title'),
		'ref':request.GET.get('ref'),
		'color':request.GET.get('color'),
		'size':request.GET.get('size'),
		'qty':request.GET.get('qty'),
		'price':request.GET.get('price'),
		'cat':request.GET.get('cat'),
		'vendor':request.GET.get('vendor'),
		'stock':request.GET.get('stock')	
	}
	if 'cartdata' in request.session:
		if str(request.GET.get('id')) in request.session['cartdata']:
			cart_data=request.session['cartdata']
			cart_data[str(request.GET.get('id'))]['qty']=int(cart_p[str(request.GET.get('id'))]['qty'])
			cart_data[str(request.GET.get('id'))]['size']=str(cart_p[str(request.GET.get('id'))]['size'])
			cart_data[str(request.GET.get('id'))]['price']=str(cart_p[str(request.GET.get('id'))]['price'])
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

	if 'cartdata' in request.session:
		for p_id,item in request.session['cartdata'].items():
			total_amt+=int(item['qty'])*float(item['price'])

			product = get_object_or_404(Product, id= p_id)

			if product.number < int(item['qty']):
				cart_data=request.session['cartdata']
				del request.session['cartdata'][p_id]
				request.session['cartdata']=cart_data
				return redirect('cart')

		prods = Product.objects.all()

		return render(request, 'cart.html',
			{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,'prods':prods})
	else:
		return render(request, 'cart.html',{'cart_data':'','totalitems':0,'total_amt':total_amt})	

def delete_cart_item(request):
	total_amt=0	
	p_id=str(request.GET.get('id'))
	if 'cartdata' in request.session:
		if p_id in request.session['cartdata']:
			cart_data=request.session['cartdata']
			del request.session['cartdata'][p_id]
			request.session['cartdata']=cart_data

	for p_id,item in request.session['cartdata'].items():
		total_amt+=int(item['qty'])*int(item['price'])

	prods = Product.objects.all()	
	t=render_to_string('ajax/cart-list.html',
		{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,'prods':prods})
	return JsonResponse({'data':t,'totalitems':len(request.session['cartdata'])})

# Delete Cart Item
def update_cart_item(request):
	total_amt=0	
	discount=0
	p_id=str(request.GET['id'])
	p_qty=request.GET.get('qty')
	p_size = request.GET.get('size')
	p_price = request.GET.get('price')
	p_stock = request.GET.get('stock')
	if 'cartdata' in request.session:
		if p_id in request.session['cartdata']:
			cart_data=request.session['cartdata']
			cart_data[str(request.GET['id'])]['qty']= p_qty
			cart_data[str(request.GET['id'])]['size']= p_size
			cart_data[str(request.GET['id'])]['price']= p_price
			cart_data[str(request.GET['id'])]['stock']= p_stock
			request.session['cartdata']=cart_data			
	for p_id,item in request.session['cartdata'].items():
		total_amt+=int(item['qty'])*int(item['price'])

	prods = Product.objects.all()
		
	t=render_to_string('ajax/cart-list.html',
		{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,'discount':discount,'prods':prods})
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
			total_amt+=int(item['qty'])*float(item['price'])

			total = total_amt + delivery	

		if 'addform' in request.POST:
			city = request.POST.get('city')
			address2 = request.POST.get('address2')
			phone = request.POST.get('phone')
			place = request.POST.get('place')
			if CustomerAddress.objects.filter(user=request.user, city=city, address=address2, phone=phone, name=place).exists():
				redirect('checkout')
			else:	
				CustomerAddress.objects.create(user=request.user, city=city, address=address2, phone=phone, name=place)
				
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
						ref=item['ref'],
						image= item['img'],
						qty=item['qty'],
						price=item['price'],
						total=float(item['qty'])*float(item['price']),
						size= item['size'],
						color= item['color'],
						vendor= item['vendor'],
						)					

			coupon = CouponCode.objects.filter(code = code)
			if coupon:
				usedcode = UsedCoupon.objects.filter(user=request.user.username, code=code).exists()
				if usedcode:
					discount=0
				else:
					for c in coupon:
						discount = int(c.per_off) * order.total_amt/100
						UsedCoupon.objects.create(user=request.user.username, code=c.code)	
			elif coupon == None:
				discount=0

			city = CustomerAddress.objects.get(pk=address)	
			city_price = City.objects.get(name = city.city)
			delivery = city_price.price		

			tot = order.total_amt + delivery - discount

			vat_fee = tot * 2/100

			total = tot + vat_fee	

			order.discount = discount
			order.delivery = delivery
			order.total = total
			order.save()

			if address is not None:
				payment = Payment.objects.create(
					order=order, order_note=note, email=email, customer=customer, address_id=address, discount=discount, amount=total, payment_option=payment_choice
					)
			else:
				payment=[]
				messages.error(request,"Delivery Address Is Required!!!")
				return redirect('checkout')	

			for p_id,item in request.session['cartdata'].items():
				p = get_object_or_404(Product, ref= item['ref'])
				p.sales = p.sales+int(item['qty'])
				p.save()

				prod = Product.objects.get(ref= item['ref'])
				prod.number = prod.number- int(item['qty'])
				prod.save()	

			order_received(order, discount, delivery, total, request.user.email)

			if payment_choice == 'Cash':

				return render(request, 'by_cash.html',
					{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'order':order,
					 'payment':payment,'delivery':delivery,'discount':discount,'total':total,'address':address,'vat':vat_fee})

			elif payment_choice == 'Transfer':

				return render(request, 'by_transfer.html',
					{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'order':order,
					 'payment':payment,'delivery':delivery,'discount':discount,'total':total,'address':address,'vat':vat_fee })

			elif payment_choice == 'Paystack':

				return render(request, 'by_paystack.html',
					{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'order':order,
					 'payment':payment,'delivery':delivery,'discount':discount,'total':total,'address':address,'vat':vat_fee, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})
						 		 	
		return render(request, 'checkout.html',
			{'cart_data':request.session['cartdata'],'totalitems':len(request.session['cartdata']),'total_amt':total_amt,'delivery':delivery,
			'discount':discount,'total':total,'address':address})
		
	else:
		
		return render(request, 'checkout.html',
			{'cart_data':'','totalitems':0,'total_amt':total_amt,'discount':discount,'total':total,'address':address})


def delivery_price(request):
	city = request.GET.get('city')
	total_amt = request.GET.get('subtotal')
	discount = request.GET.get('discount')

	city_price = City.objects.get(name = city)
	price = city_price.price
	tot = float(total_amt) + float(discount) + float(price)
	vat_fee = tot * 2/100
	total = int(tot) + int(vat_fee)
	return render(request,'ajax/delivery_price.html', {'price':price,'total':total, 'discount':discount, 'total_amt':total_amt,'vat':vat_fee})	


def pay_success(request):
	return render(request, 'pay-success.html', {})