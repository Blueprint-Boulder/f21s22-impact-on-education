from django.urls import path

from applicant import views
from applicant.views import ApplicationCreateView, ApplicationUpdateView, ApplicationDeleteView

app_name = 'applicant'
urlpatterns = [
    path('', views.home, name='home'),
    path('apps/', views.view_applications, name='view-apps'),
    path('apps/new', ApplicationCreateView.as_view(), name='new-app'),
    path('apps/<int:pk>', views.view_application, name='view-app'),
    path('apps/<int:pk>/edit', ApplicationUpdateView.as_view(), name='edit-app'),
    path('apps/<int:pk>/delete', ApplicationDeleteView.as_view(), name='delete-app'),
    path('apps/<int:pk>/confirm-submit', views.confirm_submit_application, name='confirm-submit-app'),
    path('apps/<int:pk>/submit', views.submit_application, name='submit-app'),
]
