from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class hubinfo(models.Model):
    hubid = models.CharField(max_length=60, unique=True, primary_key=True)
    latitude = models.CharField(max_length=20, blank=True, null=True, default=None)
    longitude = models.CharField(max_length=20, blank=True, null=True, default=None)

    # def __str__(self):
        # return (str(self.hubid),str(self.latitude),str(self.longitude))

class user_info(models.Model):
    hubid = models.ForeignKey(hubinfo, on_delete=models.CASCADE)
    userid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60,blank=True, null=True, default=None)
    last_name = models.CharField(max_length=60,blank=True, null=True, default=None)
    username = models.CharField(max_length=60,blank=True, null=True, default=None)
    password = models.CharField(max_length=60,blank=True, null=True, default=None)
    email = models.EmailField(max_length=100,blank=True, null=True, default=None)
    mobile_no = models.CharField(max_length=20,blank=True, null=True, default=None)
    dateofbirth = models.DateField(null=True, blank=True, default=None)

    # def __str__(self):
        # return (str(self.hubid),str(self.userid),str(self.first_name),str(self.last_name),str(self.username),str(self.password),str(self.email),str(self.mobile_no),str(self.dateofbirth))

class loginfo(models.Model):
    hubid = models.ForeignKey(hubinfo, on_delete=models.CASCADE)
    switchname = models.CharField(max_length=40)
    timestamp = models.DateTimeField(blank=True, null=True, default=None)
    intialvalue = models.BooleanField(blank=True, null=True, default=None)
    finalvalue = models.BooleanField(blank=True, null=True, default=None)
    userid = models.AutoField(primary_key=True)

    # def __str__(self):
        # return (str(self.hubid),str(self.switchname),str(self.timestamp),str(self.initialvalue),str(self.finalvalue),str(self.userid))
