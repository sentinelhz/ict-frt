from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
from PIL import Image
# Create your models here.


def path_and_rename(instance, filename):
    upload_to ='/media/images/'
    ext = filename.split(',')[-1]
    #get file name
    if instance.user.username:
        filename = 'User_Profile_pictures/{},{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)


class User_profile(models.Model):
    GENDER ={
        ('male', 'male'),
        ('female','female')
        }

    user_types = [
        ('executive', 'executive'),
        ('full-timer', 'full-timer'),
        ('contractual', 'contractual'),
        ('vendors', 'vendors'),
        ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    employment_type = models.CharField(max_length=20, blank=True, choices=user_types)
    employee_code = models.CharField(max_length=20, blank=True)
    reporting_office = models.CharField(max_length=15, blank=True)
    address_2 = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    designation = models.CharField(max_length=30, blank=True)
    profile_Pic = models.ImageField(upload_to=path_and_rename,verbose_name="Profile Picture", blank=True)



    def __str__(self):
        return self.user.username + 'User_profile'

    #def save(self, *args, **kwargs):
        #super().save(*args,**kwargs)


class PostInput(models.Model):
    name = models.CharField(max_length=200)
    hour = models.CharField(max_length=10)
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class MobileInput(models.Model):
    name = models.CharField(max_length=200)
    timestamp = models.CharField(max_length=200)

    def __str__(self):
        return self.name
