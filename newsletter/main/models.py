from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Visitor(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now=True)