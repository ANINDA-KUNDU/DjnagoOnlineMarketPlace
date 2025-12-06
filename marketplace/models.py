from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Item(models.Model):
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "items")
    name = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = "item/", null = True, blank = True)
    price = models.IntegerField()
    description = models.TextField()
    is_sold = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name