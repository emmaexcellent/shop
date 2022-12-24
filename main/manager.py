

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage



def forget_password_email(email, token):
	subject = "Your forget password link"
	message = f"Hi, click on the link to reset your password https://excelcart-production.up.railway.app/accounts/reset-password/{token}/"
	email_from = settings.EMAIL_HOST_USER
	receiver = [email]
	send_mail(subject, message, email_from, receiver)
	return True



def change_password_success(name ,email):
	subject = "Password Changed"
	message = f"Hi {{name}}, Your password have been changed successfully"
	email_from = settings.EMAIL_HOST_USER
	receiver = [email]
	send_mail(subject, message, email_from, receiver)
	return True	
