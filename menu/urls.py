from django.contrib import admin
from django.urls import path
from .views import list_menu_items

urlpatterns = [
    path('menu/',list_menu_items),
    
]
