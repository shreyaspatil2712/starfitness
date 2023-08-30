from django.db import models

class LoginData(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        app_label = 'fitness_app'


class Customer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    class Meta:
           app_label = 'fitness_app'

class Trainer(models.Model):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    speciality = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    phone_number = models.CharField(max_length=10)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
   
    class Meta:
           app_label = 'fitness_app'

class Booking(models.Model):
    customer = models.CharField(max_length=100)
    trainer = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField()
    class Meta:
           app_label = 'fitness_app'
