from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='index'),
    path('show_task/', views.show_task, name='show_task'),
    path('create_task/', views.create_task, name='create_task'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('download_task_csv/', views.download_task_csv, name='download_task_csv'),
    path('download_task_json/', views.download_task_json, name='download_task_json'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.registration, name='register'),
]