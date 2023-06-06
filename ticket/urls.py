
from .views import *
from django.urls import path
app_name = 'ticket'

urlpatterns = [
    path('', home, name='home'),
    path('create-ticket/', create_ticket,  name='create-ticket'),

]
