from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from accounts import views

app_name = "accounts"
urlpatterns = [
    # Most URLs here are copied from the URLs in django.contrib.auth.urls, with slight changes
    #  (e.g. the URLs here separated by dashes instead of underscores)
    #  Django's documentation for django.contrib.auth.urls:
    #  https://docs.djangoproject.com/en/3.2/topics/auth/default/#module-django.contrib.auth.views
    #  The URLs 'register/' and 'save_user/' are not copied from there.

    path('login/', views.LoginView.as_view(), name='login'),

    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password-change/', views.PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password-change-done'),

    path('password-reset/', views.PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/done', views.PasswordResetEmailSentView.as_view(), name='password-reset-email-sent'),
    path('reset/<uidb64>/<token>/', views.PasswordResetEnterNewPasswordView.as_view(),
         name='password-reset-new-password'),
    path('reset/done', views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),

    path('register/', views.register, name='register'),
    path('save-user/', views.save_user, name='save-user'),

    # TODO (low priority): Move the homepage-redirect URL from django_root to here (along with its view)
]