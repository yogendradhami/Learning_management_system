from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Teacher)
admin.site.register(models.CourceCategory)
admin.site.register(models.Cource)
admin.site.register(models.Student)

