from django.contrib import admin
from .models import*

# Register your models here.


class PaymentAdmin(admin.ModelAdmin):
	list_display=('customer','amount','payment_option','verified')
	list_editable=('verified',)
	search_fields = ("order__code__icontains","customer__icontains", )
admin.site.register(Payment,PaymentAdmin)