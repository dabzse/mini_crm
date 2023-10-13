from django.db import models

# Create your models here.
class Customer(models.Model):
    username    =    models.CharField(max_length=30)
    first_name  =    models.CharField(max_length=50)
    last_name   =    models.CharField(max_length=50)
    email       =    models.CharField(max_length=200)
    avatar      =    models.ImageField(upload_to="avatars/", blank=True, null=True)
    created_at  =    models.DateTimeField(auto_now_add=True)
    updated_at  =    models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}"
