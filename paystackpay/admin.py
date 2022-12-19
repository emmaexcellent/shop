from django.contrib import admin
from .models import*

# Register your models here.


class PaymentAdmin(admin.ModelAdmin):
	list_display=('customer','amount','payment_option','verified')
	list_editable=('verified',)
admin.site.register(Payment,PaymentAdmin)