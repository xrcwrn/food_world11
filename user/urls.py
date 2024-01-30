from django.urls import path
from .views import register_user, user_login, user_logout
from . import views

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('test1/', views.user_okcheck, name='test1'),
    path('reset-password/', views.password_reset, name='resetPassword'),
    path('reset-mobileno/', views.mobileNo_reset, name='resetMobileNo'),
    path('reset-emailid/', views.email_reset, name='resetEmailId')
]