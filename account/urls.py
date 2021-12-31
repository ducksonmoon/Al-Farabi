from django.urls import path
from account.views import *

urlpatterns = [
    path('university/create/', university_create, name='university_create'),
]
