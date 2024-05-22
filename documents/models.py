import uuid
from django.conf import settings
from django.db import models

class UserDocuments(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    doc_name = models.CharField(max_length=100)
    doc_url  = models.FileField(null=True, blank=True, upload_to="cond_docs/")
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)

class CondominiumDocuments(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_url = models.FileField(null=True, blank=True, upload_to="cond_docs/")
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)