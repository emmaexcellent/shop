from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    path('become-seller', views.become_seller, name="become-seller"),
    path('register', views.seller_reg, name="seller-form"),
    path('dashboard', views.vendor_dashboard, name="vendor-dashboard"),
    path('list', views.vendor_list, name="vendor-list"),
    path('<name>', views.vendor_detail, name="vendor-detail"),

    path('register/confirm-email/<token>/',views.confirm_email, name='confirm-email'),

    path('new/add-product', views.add_product, name='add-product')

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)