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

from django.urls import path, include
from User import views 
app_name = "WebUser"

urlpatterns = [
    path('HomePage/',views.homepage,name='HomePage'),
    path('TicketBooking/',views.ticketbooking,name='TicketBooking'),
    path('ViewTicketBooking/',views.viewticketbooking,name='ViewTicketBooking'),
    path('cancel-booking/', views.cancel_booking, name='cancel_booking'),
    path('payment_section/', views.payment_section, name='payment_section'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('reschedule_event/', views.reschedule_event, name='reschedule_event'),
    path('Ajaxrate/',views.ajaxrate,name="Ajaxrate"),
    path('service/', views.service_detail, name='service_detail'),
    path('ChangePassword/', views.changepassword, name='ChangePassword'),
    path('MyProfile/',views.myprofile,name='MyProfile'),
    path('EditProfile/',views.editprofile,name='EditProfile'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('EventList/', views.eventlist, name='EventList'),
    path('EventBooking/<int:did>/', views.eventbooking, name='eventbooking'),
    path('payment_process/', views.payment_process, name='payment_process'),
    path('payment_callback/', views.payment_callback, name='payment_callback'),
    path('ViewEventBooking/',views.vieweventbooking,name='vieweventbooking'),
    path('cancel_events/', views.cancel_events, name='cancel_events'),
    path('cancel-event/', views.cancel_event, name='cancel_event'),

    path('concession/', views.concession, name='concession'),

    # path('Foodapp/', include('Foodapp.urls')),
    # path('', views.home, name='Homefd'),
    
    
    # path('customer/', views.customer, name='customer'),
    # path('addtocart/', views.addtocart, name='addtocart'),
    # path('cus_search_menu/', views.cus_search_menu, name='cus_search_menu'),
    # path('cart/', views.cart, name='cart'),
    # path('viewcart/', views.viewcart, name='viewcart'),
    # path('buy/', views.buy, name='buy'),
    # path('delete_buy/', views.delete_buy, name='delete_buy'),
    # path('user_logout/', views.user_logout, name='user_logout'),

]
