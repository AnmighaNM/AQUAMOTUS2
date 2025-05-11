"""
URL configuration for WaterMetro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Foodapp import views 
app_name = "WebFoodapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

    path('canteen/', views.canteen, name='canteen'),
    path('add_category/', views.add_category, name='add_category'),
    path('delete_category/', views.delete_category, name='delete_category'),

    path('add_menu/', views.add_menu, name='add_menu'),
    path('view_menu', views.view_menu, name='view_menu'),
    path('delete_menu/', views.delete_menu, name='delete_menu'),
    path('edit_menu/', views.edit_menu, name='edit_menu'),
    path('update_menu/', views.update_menu, name='update_menu'),
    path('search_menu/', views.search_menu, name='search_menu'),
    
    path('logout/', views.logout, name='logout'),


    path('customer/', views.customer, name='customer'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('cus_search_menu/', views.cus_search_menu, name='cus_search_menu'),
    path('cart/', views.cart, name='cart'),
    path('viewcart/', views.viewcart, name='viewcart'),
    path('buy/', views.buy, name='buy'),
    path('delete_buy/', views.delete_buy, name='delete_buy'),
    path('user_logout/', views.user_logout, name='user_logout'),
]