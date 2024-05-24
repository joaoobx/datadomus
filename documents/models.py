from django.conf import settings
from django.db import models

class UserDocuments(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Usuário", 
    )
    doc_name = models.CharField(verbose_name="Nome", max_length=100)
    doc_url  = models.FileField(verbose_name="Documento", null=False, blank=False, upload_to="user_docs/")
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)

class CondominiumDocuments(models.Model):
    doc_name = models.CharField(verbose_name="Nome", max_length=100)
    doc_url = models.FileField(verbose_name="Documento", null=False, blank=False, upload_to="cond_docs/")
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)