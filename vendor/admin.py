from django.contrib import admin
from .models import *

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
	list_display=('name','image_tag','phone','email','approve')
	list_editable=('approve',)
admin.site.register(Vendor,VendorAdmin)

admin.site.register(VendorToken)

class VendorPayoutAdmin(admin.ModelAdmin):
	list_display=('vendor','amount','status','date')
	list_editable=('status',)
admin.site.register(VendorPayout,VendorPayoutAdmin)

admin.site.register(VendorWallet)
admin.site.register(VendorPayment)

admin.site.register(VendorReview)

