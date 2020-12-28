from django.urls import path

from locale_backend.core.views import *

urlpatterns = [
    path('create_booking/', BookingListCreateView.as_view())
]