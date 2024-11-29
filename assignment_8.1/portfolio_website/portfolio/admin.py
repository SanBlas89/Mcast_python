from django.contrib import admin
from .models import Project, BlogPost, Contact

admin.site.register(Project)
admin.site.register(BlogPost)
admin.site.register(Contact)