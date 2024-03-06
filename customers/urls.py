from django.urls import path
from customers import views

urlpatterns = [
    
    path('login/',views.login),
    path('register/',views.register)
]