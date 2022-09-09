from django.urls import path
from .views import home, blog_create, blog_update, blog_delete, about

urlpatterns = [
    path('', home, name = 'home'),
    path('add/', blog_create, name='add'),
    path('update/<int:id>', blog_update, name='update'),
    path('delete/<int:id>', blog_delete, name='delete'),
    path('about/', about, name='about')

]