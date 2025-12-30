from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:id>/update/', views.user_update, name='user_update'),
    path('users/<int:id>/delete/', views.user_delete, name='user_delete'),
]
