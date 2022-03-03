from django.urls import path

from applicant import views

app_name = 'applicant'
urlpatterns = [
    path('', views.home, name='home'),
    path('apps/', views.my_applications, name='my-apps'),
    path('apps/new/', views.create_application, name='new-app'),

    path('apps/scholarship/', views.my_scholarship_applications, name='my-scholarship-apps'),
    path('apps/scholarship/new/', views.ScholarshipApplicationCreateView.as_view(), name='new-scholarship-app'),
    path('apps/scholarship/<int:pk>/', views.ScholarshipApplicationDetailView.as_view(), name='view-scholarship-app'),
    path('apps/scholarship/<int:pk>/edit/', views.ScholarshipApplicationUpdateView.as_view(),
         name='edit-scholarship-app'),
    path('apps/scholarship/<int:pk>/confirm-delete/', views.ScholarshipApplicationDeleteView.as_view(),
         name='confirm-delete-scholarship-app'),
    path('apps/scholarship/<int:pk>/confirm-submit/', views.confirm_submit_scholarship_application,
         name='confirm-submit-scholarship-app'),
    path('apps/scholarship/<int:pk>/submit/', views.submit_scholarship_application, name='submit-scholarship-app'),

    path('apps/academic-funding/', views.my_academic_funding_applications, name='my-academic-funding-apps'),
    path('apps/academic-funding/new/', views.AcademicFundingApplicationCreateView.as_view(),
         name='new-academic-funding-app'),
    path('apps/academic-funding/<int:pk>/', views.AcademicFundingApplicationDetailView.as_view(),
         name='view-academic-funding-app'),
    path('apps/academic-funding/<int:pk>/edit/', views.AcademicFundingApplicationUpdateView.as_view(),
         name='edit-academic-funding-app'),
    path('apps/academic-funding/<int:pk>/confirm-delete/', views.AcademicFundingApplicationDeleteView.as_view(),
         name='confirm-delete-academic-funding-app'),
    path('apps/academic-funding/<int:pk>/confirm-submit/', views.confirm_submit_academic_funding_application,
         name='confirm-submit-academic-funding-app'),
    path('apps/academic-funding/<int:pk>/submit/', views.submit_academic_funding_application,
         name='submit-academic-funding-app'),
]
