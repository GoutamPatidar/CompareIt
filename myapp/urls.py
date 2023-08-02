from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('History/', views.History, name='History'),
    path('About/', views.About, name='About'),
    path('Contact/', views.Contact, name='Contact'),
    path('Login/', views.Login, name='Login'),
    path('Logout/', views.Logout, name='Logout'),
    path('Registration/', views.Registration, name='Registration'),
    path('Profile/', views.Profile, name='Profile'),
    path('Profile_edit/', views.Profile_edit, name='Profile_edit'),
    path('Search_product/',views.Search_product,name='Search_product'),
    path('buy_now/',views.buy_now,name='buy_now'),
    path('Check_Again/',views.Check_Again,name='Check_Again'),
    path('Contact_email/',views.Contact_email,name='Contact_email'),



    
]