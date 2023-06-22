from django.urls import path
from .views import home, auth_view, verify_view

urlpatterns = [
    path('', home, name='index'),
    path('login/', auth_view, name='login'),
    path('verify/', verify_view, name='verify'),
]