from django.contrib import admin

# Register your models here.
from main2 import models
from main2.models import Student

admin.site.register(Student)
# level = models.IntegerField(null=True, blank=True)

