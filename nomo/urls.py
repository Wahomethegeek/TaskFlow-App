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

    # ------------------- Logout a User ------------------- #
    path('user-logout', views.my_logout, name='my-logout')

]
