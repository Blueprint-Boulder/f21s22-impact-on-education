from django.urls import path

import application.views
from applicant import views
from application.views import VolunteerApplicationCreateView, CollegeApplicationCreateView

app_name = 'applicant'
urlpatterns = [
    path('', views.home, name='home'),
    path('apps/', views.my_applications, name='my-apps'),
    path('apps/new/', views.create_application, name='new-app'),
    path('apps/new/<int:app_type_pk>/', views.create_customizable_application, name='new-custom-app'),
    path('apps/edit/pk=<int:pk>&num_text_fields=<int:num_text_fields>',
         views.edit_customizable_application, name='edit-custom-app'),
    path('apps/new-field/', views.new_customizable_application_field, name='new-custom-app-field'),

    #Scholarship Application Urls
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

    #Internship Application Urls
    path('apps/internship/', views.my_internship_applications, name='my-internship-apps'),
    path('apps/internship/new/', views.InternshipApplicationCreateView.as_view(),
         name='new-internship-app'),
    path('apps/internship/<int:pk>/', views.InternshipApplicationDetailView.as_view(),
         name='view-internship-app'),
    path('apps/internship/<int:pk>/edit/', views.InternshipApplicationUpdateView.as_view(),
         name='edit-internship-app'),
    path('apps/internship/<int:pk>/confirm-delete/', views.InternshipApplicationDeleteView.as_view(),
         name='confirm-delete-internship-app'),
    path('apps/internship/<int:pk>/confirm-submit/', views.confirm_submit_internship_application,
         name='confirm-submit-internship-app'),
    path('apps/internship/<int:pk>/submit/', views.submit_internship_application,
         name='submit-internship-app'),

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
