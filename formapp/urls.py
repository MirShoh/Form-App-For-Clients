from django.urls import path
from .views import client_form, client_list

urlpatterns = [
    path('', client_form, name="client-form"),
    path('list/', client_list, name="client-list"),
]