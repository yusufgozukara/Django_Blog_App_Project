from django.urls import path
from .views import home, blog_create, blog_update

urlpatterns = [
    path('', home, name = 'home'),
    path('add/', blog_create, name='add'),
    path('update/<int:id>', blog_update, name='update')

]