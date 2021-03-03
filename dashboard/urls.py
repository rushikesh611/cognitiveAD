from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview, name='home'),
    path('dashboard',views.index, name='dashboard'),
    path('tools',views.tools, name='tools'),
]