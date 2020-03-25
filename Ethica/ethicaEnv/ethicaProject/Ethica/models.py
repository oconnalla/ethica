from django.db import models
from django.contrib.auth.models import User


#Model 1 of 4
class Businesses(models.Model):
    Business_title=models.CharField(max_length=255)
    meeting_date=models.DateField()
    meeting_time=models.TimeField()
    location=models.CharField(max_length=255, null=True, blank=True)
    agenda=models.CharField(max_length=255, null=True, blank=True)

    #####METHOD###################
    def __str__(self):
        return self.meeting_title 
    
    class Meta:
        db_table='Business'
        verbose_name_plural='Businesses'