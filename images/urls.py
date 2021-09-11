from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_out/', views.sign_out, name='sign_out'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='images/reset_password/reset_password.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='images/reset_password/reset_password_done.html'), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='images/reset_password/reset_password_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='images/reset_password/reset_password_complete.html'), name='password_reset_complete'),
    
    path('', views.home, name='home'),
    path('my-images/', views.my_images, name='my_images'),
    path('delete/<int:pk>/', views.delete_img, name='delete_img'),
    path('image/<int:pk>/', views.image, name='image'),
]