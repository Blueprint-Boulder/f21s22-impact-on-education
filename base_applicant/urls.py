"""
LIST OF URLS TO IMPLEMENT FOR APPLICANT APPS (apps in the programming sense)

[empty URL] (name: "home") - The homepage.
apps/ (name: "view-apps") - List of the user's applications.
apps/new/ (name: "create-app") - Page for creating a new application.
apps/<int:pk>/ (name: "view-app") - View of a single application.
apps/<int:pk>/edit/ (name: "edit-app") - Page for editing an existing application.
apps/<int:pk>/confirm-delete/ (name: "confirm-delete-app") -
  Page to confirm whether to delete an application.
  If confirmed, deletes the application, and redirects to a page that indicates the deletion was successful.
apps/<int:pk>/confirm-submit/ (name: "confirm-submit-app") -
  Submit confirmation page.
  If confirmed, submits the application, and redirects to a page that indicates the submission was successful.
"""
