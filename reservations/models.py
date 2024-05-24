from django.conf import settings
from django.db import models

class CarReservations(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Usuário", 
    )
    tenant_name = models.CharField(verbose_name="Locatário", max_length=100)
    apartment = models.CharField(verbose_name="Apartamento", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)

class SpaceReservations(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Usuário", 
    )
    description = models.CharField(verbose_name="Descrição", max_length=100)
    apartment = models.CharField(verbose_name="Apartamento", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)