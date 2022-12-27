from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager
# Create your models here.

class UserAcc(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(unique=True, primary_key=True)
    password = models.CharField(max_length=100)
    credit = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    package = models.CharField(max_length=20, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS: list(['firstname','lastname','email','password'])

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class packages(models.Model):
    name = models.CharField(max_length=20)
    value = models.IntegerField(default=0)
    price = models.CharField(max_length=10,default='')
    cycle = models.CharField(max_length=20,default='')
    limited_offer_desc = models.CharField(max_length=150, blank=True)
    desc1 = models.CharField(max_length=150)
    desc2 = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class notes(models.Model):
    owner = models.ForeignKey(UserAcc, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    text = models.TextField()

    def __str__(self):
        return str(self.id)

class dataset(models.Model):
    complex_text = models.TextField()
    simple_text = models.TextField()

    def __str__(self):
        return str(self.complex_text)

class ChatBot(models.Model):
    user = models.ForeignKey(UserAcc, on_delete=models.CASCADE, default=1)
    user_input = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)