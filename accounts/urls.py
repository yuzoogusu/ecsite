from django.urls import path
from accounts import views

urlpatterns = [
    path('profile/', views.ProfileVies.as_view(), name='profile'),
]