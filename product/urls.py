from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'product'

urlpatterns = [
    path('<str:category_title>/<str:slug>-<str:id>', views.detail, name="detail"),    

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)