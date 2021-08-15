from django.urls import path
from . import views
urlpatterns = [
    path('', views.english, name='ENGLISH'),
    path('login/', views.login, name='LOGIN'),
    path('identify/', views.passwtv, name='PASSVERGESSEN'),
]