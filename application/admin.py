from django.contrib import admin

from application.models import Application, School, CustomizableApplication

admin.site.register(Application)
admin.site.register(CustomizableApplication)
admin.site.register(School)
