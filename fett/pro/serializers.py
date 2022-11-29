from django.db.models import fields
from rest_framework import serializers
from .models import requirement
  
class requirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = requirement
        fields = ['id','company_name','company_email','project_name', 'offer_price', 'duration', 'needed_skills','description', 'expire_date']