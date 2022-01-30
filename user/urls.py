from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('password-reset/', auth_views.PasswordResetView.as_view(template_name='user/resetPW.html'), name="password_reset"),
   path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='user/completePW.html'), name = "password_reset_done"),
   path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/resetPWConfirm.html'), name="password_reset_confirm"),
   #path('emailsent/', views.emailsent, name="user-emailsent"),
   #path('security/', views.security, name = "user-security")
]