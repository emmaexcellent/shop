from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import *


class ReviewAdd(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["rating"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'name':"rating",
			'id': "id_rating"
			})
		self.fields["text"].widget.attrs.update({
			'required':'',
			'class':"form-control",
			'name':"text",
			'id': "id_text",
			'cols':"4o",
			'rows': "10",
			'placeholder': "Leave a comment here"
			})
	class Meta:
		model=Review
		fields=('text','rating')