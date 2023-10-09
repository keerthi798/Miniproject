from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from.import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('',views.index,name="index"),
   path('signup/',views.signup, name="signup"),
   path('login/', views.login, name="login"),
   path('dashboard/',views.dashboard,name="dashboard"),
   path('logout/', views.logout_confirm,name='logout'),
   path('booking/', views.booking, name='booking'),

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]