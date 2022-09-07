from django.urls import path, include
from .views import register, user_login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logouts/', LogoutView.as_view(), name='logout_app'),
]