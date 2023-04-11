
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/admin/admin/030/', admin.site.urls),
    path('', include('main.urls')),
    path('shop/', include('product.urls')),
    path('', include('cart.urls')),
    path('payment/', include('paystackpay.urls')),
    path('vendor/', include('vendor.urls')),

    path('www.excelcart.com.ng', RedirectView.as_view(url='excelcart.com.ng/', permanent=True)),
    path('www.excelcart.org', RedirectView.as_view(url='excelcart.com.ng/', permanent=True)),
    path('www.excelcart.com', RedirectView.as_view(url='excelcart.com.ng/', permanent=True)),
    path('www.excelcart.net', RedirectView.as_view(url='excelcart.com.ng/', permanent=True)),
    path('www.excelcart.shop', RedirectView.as_view(url='excelcart.com.ng/', permanent=True)),
    path('excelcart.shop', RedirectView.as_view(url='excelcart.com.ng/', permanent=True)),
    path('excelcart.com', RedirectView.as_view(url='excelcart.com.ng/', permanent=True)),
]
