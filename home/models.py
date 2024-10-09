from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator



class FooterItem(models.Model):
    item_title = models.CharField(max_length=50)
    item_description = RichTextField()
    item_icon = models.CharField(max_length=100, null= True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)

    is_visible = models.BooleanField(default=True)
    sort = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __iter__(self):
        dishes = self.dishes.filter(is_visible=True).order_by('sort')
        for dish in dishes:
            yield dish

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

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')

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
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='gallery')
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
     item_title = models.CharField(max_length=50)
     item_description = RichTextField()
     item_icon = models.CharField(max_length=50)

     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     def __str__(self):
         return self.item_title


class Reservation(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?3?\d{9,15}$',
    message='Phone number must be entered in the format: +39999999999')

    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150, validators=[phone_regex])
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_processed = models.BooleanField(default=False)
    def __str__(self):
        return self.name

