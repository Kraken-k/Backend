from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin ,BaseUserManager


class UserAccountManager(BaseUserManager):

    def create_user(self,email,name,password=None):
        if not (email):
            raise ValueError("User must have a email ")
        
        email = self.normalize_email(email)
        name = name
        user = self.model(email=email,name = name)
        user.set_password(password)
        user.save()

        return user
    

class UserAccounts(AbstractBaseUser,PermissionsMixin): 
    email=models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_admin= models.BooleanField(default=False)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserAccountManager()

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email

# Create your models here.
