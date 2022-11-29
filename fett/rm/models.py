from django.db import models

# Create your models here.
class forum(models.Model):
    project_name=models.CharField(max_length=200,null=True)
    about_project=models.CharField(max_length=1000,null=True)
    required_skills=models.CharField(max_length=500,null=True)
    bid=models.CharField(max_length=10000,null=True)
    document=models.FileField(upload_to='document',null=True)
    email=models.CharField(max_length=200,null=True)
    phone_no=models.CharField(max_length=13,null=True)

    def __str__(self):
        return self.project_name
