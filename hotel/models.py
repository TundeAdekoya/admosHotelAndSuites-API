from django.db import models
from django.contrib.auth.models import User 

# Create your models here.


class Room_service(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False) 
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
       return self.name

class Event_service(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False) 
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
       return self.name

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    payment_method = models.CharField(max_length=200, null=True, blank=True)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_checkedin = models.BooleanField(default=False)
    checked_in_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False) 

    def __str__(self):
        return str(self.created_at)

class Room_booking(models.Model):
    service = models.ForeignKey(Room_service, on_delete=models.SET_NULL, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    no_of_children = models.IntegerField(default=0, null=True, blank=True)
    no_of_adults = models.IntegerField(default=0, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False) 

    def __str__(self):
        return self.name


class Event_booking(models.Model):
    service = models.ForeignKey(Event_service, on_delete=models.SET_NULL, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    no_of_people = models.IntegerField(default=0, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False) 

    def __str__(self):
        return self.name


class Contact_detail(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False) 

    def __str__(self):
        return str(self.phone_number)
