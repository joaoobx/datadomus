from django.conf import settings
from django.db import models

class ServiceOrders(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    image_url = models.CharField(max_length=100) 
    title = models.CharField(max_length=100) 
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    read_at = models.DateTimeField(null=True)
    finished_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)
