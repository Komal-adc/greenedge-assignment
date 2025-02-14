from datetime import timedelta, datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number field must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(phone_number, password, **extra_fields)

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=50, unique=False, blank=True, null=True)
    membership_type = models.CharField(max_length=10, choices=[
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Diamond', 'Diamond'),
    ], default='Silver')
    membership_start_date = models.DateField(null=True, blank=True)  # Remove auto_now_add
    membership_expiry_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.membership_start_date:
            self.membership_start_date = datetime.today().date()  # Set default start date

        if not self.membership_expiry_date:
            if self.membership_type == 'Silver':
                self.membership_expiry_date = self.membership_start_date + timedelta(days=30)
            elif self.membership_type == 'Gold':
                self.membership_expiry_date = self.membership_start_date + timedelta(days=90)
            elif self.membership_type == 'Diamond':
                self.membership_expiry_date = self.membership_start_date + timedelta(days=180)

        super().save(*args, **kwargs)






