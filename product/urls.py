from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('<str:category_title>/<str:slug>-<str:id>', views.detail, name="detail"), 
    path('subcat', views.listsub_cat, name="sub_cat" )   

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)