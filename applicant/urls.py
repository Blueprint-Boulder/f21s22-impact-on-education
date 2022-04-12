from django.urls import path

from applicant import views
from application.views import VolunteerApplicationCreateView, CollegeApplicationCreateView

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

    #Volunteer Application Urls
    path('apps/volunteer/', views.my_volunteer_applications, name='my-volunteer-apps'),
    path('apps/volunteer-app/new', VolunteerApplicationCreateView.as_view(),
         name='new-volunteer-app'),
    path('apps/volunteer-app/<int:pk>/', views.VolunteerApplicationDetailView.as_view(),
         name='view-volunteer-app'),
    path('apps/volunteer/<int:pk>/edit/', views.VolunteerApplicationUpdateView.as_view(),
             name='edit-volunteer-app'),
    path('apps/volunteer-app/<int:pk>/confirm-delete/', views.VolunteerApplicationDeleteView.as_view(),
         name='confirm-delete-volunteer-app'),
    path('apps/volunteer-app/<int:pk>/confirm-submit/', views.confirm_submit_volunteer_application,
             name='confirm-submit-volunteer-app'),
    path('apps/volunteer/<int:pk>/submit/', views.submit_volunteer_application, name='submit-volunteer-app'),

    #College Application Urls
    path('apps/college/', views.my_college_applications, name='my-college-apps'),
    path('apps/college-app/new', CollegeApplicationCreateView.as_view(),
         name='new-college-app'),
    path('apps/college-app/<int:pk>/', views.CollegeApplicationDetailView.as_view(),
         name='view-college-app'),
    path('apps/college/<int:pk>/edit/', views.CollegeApplicationUpdateView.as_view(),
             name='edit-college-app'),
    path('apps/college-app/<int:pk>/confirm-delete/', views.CollegeApplicationDeleteView.as_view(),
         name='confirm-delete-college-app'),
    path('apps/college-app/<int:pk>/confirm-submit/', views.confirm_submit_college_application,
             name='confirm-submit-college-app'),
    path('apps/college/<int:pk>/submit/', views.submit_college_application, name='submit-college-app'),
]
