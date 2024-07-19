from django.contrib import admin
from .models import ApplyAttachment, Attendance, Report

# Register your models here.
admin.site.register(Report)
admin.site.register(ApplyAttachment)
admin.site.register(Attendance)