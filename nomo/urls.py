from django.urls import path
from . import views

urlpatterns = [

    # ------------------- Home page ------------------- #
    path('', views.home, name=''),

    # ------------------- Register a User ------------------- #
    path('register', views.register, name='register'),

    # ------------------- Login a User ------------------- #
    path('login', views.my_login, name='my-login'),

    # ------------------- Dashboard a User ------------------- #
    path('dashboard', views.dashboard, name='dashboard'),

    # ------------------- profile management ------------------- #
    path('profile', views.profile, name='profile'),

    # ------------------- profile management ------------------- #
    path('delete_profile', views.deleteProfile, name='delete_profile'),

    # ------------------- create a task------------------- #
    path('create-task', views.createTask, name='create_task'),

    # ------------------- Read a task------------------- #
    path('view_task', views.viewTask, name='view_task'),

    # ------------------- Read a task------------------- #
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),

    # ------------------- Read a task------------------- #
    path('delete_task/<str:pk>/', views.deleteTask, name='delete_task'),

    # ------------------- Logout a User ------------------- #
    path('user-logout', views.my_logout, name='my-logout'),
]
