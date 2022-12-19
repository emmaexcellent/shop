from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib import messages

# Create your views here.

def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
	payment = get_object_or_404(Payment, ref=ref)
	verified = payment.verify_payment()
	if verified:
		messages.success(request, "Verification Successful")
	else:
		messages.error(request, "Verification Failed!")	
	return redirect('checkout')