from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from cart.models import *
from vendor.models import *
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib import messages

# Create your views here.

def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
	payment = get_object_or_404(Payment, ref=ref)
	verified = payment.verify_payment()
	if verified:
		items = CartOrderItems.objects.filter(order = payment.order)
		for i in items:
			wallet = VendorWallet.objects.get(vendor__name = i.vendor)
			wallet.balance = int(wallet.balance) + int(i.total)
			wallet.save()
		messages.success(request, "Verification Successful")
		return redirect('pay-success')
	else:
		messages.error(request, "Payment Verification Failed!")	
		return redirect('checkout')