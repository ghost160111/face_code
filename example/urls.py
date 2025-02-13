# example/urls.py
from django.urls import path

from example.views import index, ContactCreateAPIView

urlpatterns = [
    path('', index),
    path('contacts/', ContactCreateAPIView.as_view(), name='contact-create'),
]