from django.contrib import admin

from student.models import ScholarshipApplication, FileAndPerms

admin.site.register(ScholarshipApplication)
admin.site.register(FileAndPerms)
