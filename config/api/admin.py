from django.contrib import admin
from .models import Job, Comment, Category

admin.site.register([Job, Comment, Category])
