from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name="home"),
    path('shop', views.shop, name="shop"),
    path('search', views.search, name="search"),
    path('shop/<str:title>-<int:cat_id>', views.category_product_list, name="category"),
    path('accounts/register', views.registerUser, name="register"),
    path('accounts/login/', views.loginView, name="login"),
    path('accounts/logout', views.logoutUser, name="logout"),
    path('accounts/dashboard', views.user_dash, name="user-dashboard"),
    path('contact-us', views.contact, name="contact"),
    path('about-us', views.about_us, name="about"),
    path('faq', views.faq, name="faq"),
    path('order-tracking', views.order_tracking, name="order-tracking"),

    path('accounts/forgot-password',views.forgot_password, name='forgot-password'),
    path('accounts/reset-password/<token>/',views.reset_password, name='reset-password'),
    path('accounts/change-password', views.change_password, name='change-password')
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)