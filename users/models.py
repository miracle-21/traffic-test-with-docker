from ipaddress import ip_address
from django.db import models

# Create your models here.
class User(models.Model):
    name       = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    ip_address = models.GenericIPAddressField(null=True)
    

    class Meta:
        db_table = 'users'