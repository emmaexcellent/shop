from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CouponCode)
admin.site.register(Wishlist)
admin.site.register(Tracking)

class CustomerAddressAdmin(admin.ModelAdmin):
	list_display=('user','phone','name')
	search_fields = ("name__icontains","user__username__icontains", )
admin.site.register(CustomerAddress,CustomerAddressAdmin)

class CartOrderAdmin(admin.ModelAdmin):
	list_editable=('paid_status','order_status')
	list_display=('id','user','total_amt','paid_status','order_dt','order_status')
	search_fields = ("id__icontains","user__username__icontains", )
admin.site.register(CartOrder,CartOrderAdmin)

class CartOrderItemsAdmin(admin.ModelAdmin):
	list_display=('invoice_no','item','image_tag','qty','price','vendor','total')
	search_fields = ("invoice_no__icontains", )
admin.site.register(CartOrderItems,CartOrderItemsAdmin)