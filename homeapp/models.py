from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, fname, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff') is not True:
            raise ValueError("is_staff=False -> Precisa de ser True")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("is_superuser=False -> Precisa de ser True")
        
        return self.create_user(email, username, fname, password, **other_fields)
    
    def create_user(self, email, username, fname, password, **other_fields):
        
        if not username:
            raise ValueError(_("Introduz um Username válido"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, fname=fname, **other_fields)
        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=30, unique=True)
    username = models.CharField(max_length=30, unique=True)
    fname = models.CharField(max_length=30)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'fname']
    
    def __str__(self):
        return self.fname
    
    
class Task(models.Model):
    tname = models.CharField(max_length=30)
    tdate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.tname
    
class Produto(models.Model):
    pname = models.CharField(max_length=20)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.pname