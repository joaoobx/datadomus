from django.conf import settings
from django.db import models

class ServiceOrders(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    image_url = models.ImageField(null=True, blank=True, upload_to="service_orders/") 
    title = models.CharField(verbose_name="Título", max_length=100) 
    description = models.CharField(verbose_name="Descrição", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    read_at = models.DateTimeField(null=True)
    finished_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)
