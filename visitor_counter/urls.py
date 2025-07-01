from django.urls import path
from .views import increment_counter

urlpatterns = [
    path('increment/', increment_counter, name='increment_counter'),
]