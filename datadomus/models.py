import uuid
from django.db import models

class Users(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    email = models.CharField(null=False, max_length=100, blank=False)
    name = models.CharField(null=False, max_length=100, blank=False)
    apartment = models.CharField(null=False, max_length=100, blank=False)
    phone = models.CharField(null=False, max_length=100, blank=False)
    password = models.CharField(null=False, max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()