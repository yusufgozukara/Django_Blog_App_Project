from django.urls import path
from .views import home, blog_create

urlpatterns = [
    path('', home, name = 'home'),
    path('add/', blog_create, name='add')

]