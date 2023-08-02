from django.db import models
import datetime


class profile_data(models.Model):
     Username=models.CharField(max_length=50,default="")
     Mobile = models.CharField(max_length=50, default="")
     Email = models.EmailField(max_length=50, default="")
     Age = models.IntegerField()
     Address = models.CharField(max_length=200, default="")
     Password = models.CharField(max_length=200, default="")
    

class UserHistory(models.Model):
     
     Email=models.EmailField( max_length=254,default="")
     Username=models.CharField( max_length=50, default="")
     Product_name=models.CharField( max_length=50, default="")
     DateTime=models.DateTimeField(auto_now_add=True)

     