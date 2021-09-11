from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random
import json
from uuid import uuid4

class MyAccountManager(BaseUserManager):
    def create_user(self,username, email, password=None):
        if not email:
            raise ValueError('email is required')
        if not username:
            raise ValueError('username is required')
        
        user = self.model(
            email= self.normalize_email(email),
            username= username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email,password):
        user = self.create_user(
             email= self.normalize_email(email),
            username= username,
            password= password,
        
        )
        user.is_admin=True
        user.is_superuser=True
        user.is_staff= True
        user.save(using=self._db)
        return user





def rand_str():
      return str(uuid4()).replace('-', '')[:30]


class Account(AbstractBaseUser):
    email       = models.EmailField(verbose_name='email', max_length=60, unique=True )
    username    = models.CharField(max_length=30, unique=True)
    fullname    = models.CharField(max_length=100, blank=True,null=True)
    postalcode    = models.CharField(max_length=30,blank=True,null=True)
    country    = models.CharField(max_length=100,blank=True,null=True)
    address    = models.CharField(max_length=100,blank=True,null=True)
    date_of_birth = models.CharField(max_length=30, blank=True,null=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin    = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(blank=True, null=True, default='defualt.png', upload_to='uploads')
    phone = models.CharField(max_length=30, blank=True,null=True,unique=True)
    balance = models.IntegerField(default=0, blank=True,null=True)
    withdraw_total = models.IntegerField(default=0, blank=True,null=True)
    coin_balance = models.IntegerField(default=0, blank=True,null=True)
    uri = models.CharField(max_length=50, default=rand_str(), blank=True,null=True)
    

    
    objects = MyAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def  has_module_perms(self, app_label):
        return True




class Transaction(models.Model):
    user = models.ForeignKey(Account,related_name='trans_usr', on_delete=models.CASCADE)
    transac_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    coin = models.CharField(max_length=100)
    amount_in_coin = models.IntegerField(default=0)
    amount_in_usd = models.IntegerField(default=0)
    created = models.DateTimeField( auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.status

class Buycoin(models.Model):
    user = models.ForeignKey(Account,related_name='buy_usr', on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    coin = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_in_coin = models.IntegerField(default=0)
    amount_in_usd = models.IntegerField(default=0)
    pop = models.ImageField(blank=True, null=True, upload_to='uploads')
    uri = models.CharField(max_length=50, default=rand_str(), blank=True,null=True)
    created = models.DateTimeField( auto_now_add=True,blank=True,null=True)


    def total(self):
        return int(self.amount_in_usd) + 5
    
    def __str__(self):
        return self.user.username