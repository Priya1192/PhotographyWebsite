from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='home'),
               path('ordernow', views.orders, name='index'),
               path('orders', views.addorder),
               ]