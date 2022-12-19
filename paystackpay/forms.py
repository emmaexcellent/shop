
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import *

class PaymentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["address"].widget.attrs.update({
			'required':'',
			'class':"form-check-input mt-0",
			'type':"radio", 
			'name':"address"
			})
		self.fields["Order_note"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'type':"text", 
			'name':"order_notes"
			})
		self.fields["payment_option"].widget.attrs.update({
			'required':'',
			'class':"checkout__payment__detail",
			'type':"text", 
			'name':"Payment_option"
			})

	class Meta:
		model=Payment
		fields=('amount','email','payment_option','address','customer','order_note')
		widgets = {
			'payment_option': forms.RadioSelect(),
			'address': forms.RadioSelect()
		}