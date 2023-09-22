from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('', views.home , name='homepage'),
    path('about/', views.about , name='about'),
    path('order/', views.order , name='order'),
    path('book_table/', views.book_table , name='book_table'),
    path('contact/', views.contact , name='contact'),

]
