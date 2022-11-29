from django.contrib import admin
from .models import forum


@admin.register(forum)
class forumAdmin(admin.ModelAdmin):
    
    fields = ('project_name','about_project','required_skills','bid','document')


