

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage



def forget_password_email(username,email, token):
	html_template = 'emails/forgot-password-email.html'
	html_message = render_to_string(html_template, {'username':username, 'token':token})
	subject = 'Forgot Password'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [email]
	message = EmailMessage(subject, html_message,email_from, recipient_list)
	message.content_subtype = 'html'
	message.send()
	return True	
	

def change_password_success(username,email):
	html_template = 'emails/password-changed.html'
	html_message = render_to_string(html_template, {'username':username})
	subject = 'Password Changed'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [email]
	message = EmailMessage(subject, html_message,email_from, recipient_list)
	message.content_subtype = 'html'
	message.send()
	return True	


def new_user(username, email):
	html_template = 'emails/newuser_email.html'
	html_message = render_to_string(html_template, {'username':username})
	subject = 'Welcome to Excelcart'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [email]
	message = EmailMessage(subject, html_message,email_from, recipient_list)
	message.content_subtype = 'html'
	message.send()
	return True	

