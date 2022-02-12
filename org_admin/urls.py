from django.urls import path

from org_admin import views
from org_admin.views import ScholarshipApplicationCreateViewAdmin, ScholarshipApplicationUpdateViewAdmin, ScholarshipApplicationDeleteViewAdmin


# org_admin refers to admins of the Impact on Education organization
#  (as opposed to site admins, i.e. the people that administer the website itself)
app_name = 'org_admin'
urlpatterns = [
    path('', views.home, name='home'),
    path('users', views.users, name='users'),
    path('apps/', views.all_scholarship_apps, name='view-apps'),
    path('apps/new/', ScholarshipApplicationCreateViewAdmin.as_view(), name='new-app'),
    path('apps/<int:pk>/', views.ScholarshipApplicationDetailViewAdmin.as_view(), name='view-app'),
    path('apps/<int:pk>/edit/', ScholarshipApplicationUpdateViewAdmin.as_view(), name='edit-app'),
    path('apps/<int:pk>/confirm-delete/', ScholarshipApplicationDeleteViewAdmin.as_view(), name='confirm-delete-app'),
    path('apps/<int:pk>/confirm-submit/', views.confirm_submit_application, name='confirm-submit-app'),
    path('apps/<int:pk>/submit/', views.submit_application, name='submit-app'),
]
