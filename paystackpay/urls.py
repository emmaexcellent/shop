from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('<str:ref>/', views.verify_payment, name="verify"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)