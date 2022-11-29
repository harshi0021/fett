from django.db import models

# Create your models here.
class requirement(models.Model):
    company_name= models.CharField(max_length=100)
    company_email= models.CharField(max_length=100,null=True)
    project_name = models.CharField(max_length=200,null=True,blank=True)
    needed_skills= models.CharField(max_length=500,null=True,blank=True)
    offer_price= models.CharField(max_length=1000000,null=True,blank=True)
    description=models.CharField(max_length=1000000,null=True,blank=True)
    duration=models.CharField(max_length=200,null=True,blank=True)
    expire_date=models.DateField(null=True,blank=True)
  
    def __str__(self):
        return self.company_name