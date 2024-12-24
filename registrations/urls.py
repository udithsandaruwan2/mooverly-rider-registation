
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register/s/1', views.registerStep1, name='registerStep1'),
    path('register/s/2', views.registerStep2, name='registerStep2'),
    path('register/s/3', views.registerStep3, name='registerStep3'),
    path('register/s/4', views.registerStep4, name='registerStep4'),
    
    path('register/success', views.registerSuccess, name='registerSuccess'),
    
]


