from django.db import models


# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.IntegerField()
    unit = models.CharField(max_length=10)

    photo = models.ImageField(upload_to='dishes', blank=True, null=True)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='events', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Staff(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    bio = models.TextField()
    photo = models.ImageField(upload_to='staff', blank=True, null=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.ImageField(upload_to='galleries', blank=True, null=True)

    def __str__(self):
        return self.image

class Contact(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    opening_hours = models.TextField()

    def __str__(self):
        return self.address



