from django.urls import path
from . import views
from .views import *

app_name = 'home'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('api/', CustomerList.as_view() , name='api'),
]
