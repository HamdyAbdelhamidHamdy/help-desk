
from .views import *
from django.urls import path
app_name = 'ticket'

urlpatterns = [
    path('home/', home, name='home'),
    path('', create_ticket,  name='create-ticket'),

]
