from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.RegistrationPage, name='register'),
    path('ionize/', views.Ionize, name='ionize'),
    path('entry_detail/<str:pk_test>/', views.EntryDetail, name='entry-detail'),
    path('editor/', views.Editor, name='editor'),
    path('delete/<str:pk>/',views.DeleteEntry, name='delete'),
    path('update/<str:pk>/',views.EditEntry, name='update'),
    path('privacy/', views.PrivacyPolicy, name= 'privacy'),
    path('terms/', views.TermsOfService, name='terms'),




    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="mdiary/password_reset.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="mdiary/password_reset_sent.html"), name = 'password_reset_done'), 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="mdiary/password_reset_form.html"), name='password_reset_confirm'), 
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="mdiary/password_reset_done.html"), name='password_reset_complete'), 




]
