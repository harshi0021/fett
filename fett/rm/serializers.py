from rest_framework import serializers
from .models import forum


class forumSerializer(serializers.ModelSerializer):
    class Meta:
        model = forum
       
        fields = ['id','project_name','about_project','required_skills','bid','document']