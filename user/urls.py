from django.urls import path
from . import views


urlpatterns = [
    path('login.html', views.login, name='login'),
    path('register.html', views.register, name='register'),
    path('logout.html', views.logout, name='logout'),
    path('user_info.html', views.user_info, name='user_info'),
    path('change_nickname.html', views.change_nickname, name='change_nickname'),
    path('bind_email.html', views.bind_email, name='bind_email'),
    path('send_verification_code.html', views.send_verification_code, name='send_verification_code'),
    path('change_password.html', views.change_password, name='change_password'),
    path('forgot_password.html', views.forgot_password, name='forgot_password'),
]