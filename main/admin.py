from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display=('title','image_tag',)
admin.site.register(Category,CategoryAdmin)

admin.site.register(SubCategory)
admin.site.register(Contact)
admin.site.register(Faq)
admin.site.register(UserToken)



