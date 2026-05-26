from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    # path('contact',views.contact,name='contact'),
    path('form',views.form,name='form'),
    path('result',views.result,name='result'),
    path('formedit',views.formedit,name='formedit'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT);
