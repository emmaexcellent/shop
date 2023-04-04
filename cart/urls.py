from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('add-to-cart/', views.add_to_cart, name="add_to_cart"),
    path('delete-from-cart/', views.delete_cart_item, name="delete-from-cart"),
    path('update-cart/', views.update_cart_item, name="update-cart"),
    path('cart', views.cart_list, name="cart"),  
    path('checkout', views.checkout, name="checkout"),  

    path('checkout/payment/success', views.pay_success, name="pay-success"),   


    path('add-wishlist',views.add_wishlist, name='add_wishlist'),
    path('account/dashboard/wishlist',views.wishlist, name='wishlist'),

    path('delivery_price',views.delivery_price, name='delivery'),


] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)