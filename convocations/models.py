from django.db import models

class Convocations(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100)
    description = models.CharField(verbose_name="Descrição", max_length=100)
    doc_url = models.FileField(verbose_name="Documento", null=False, blank=False, upload_to="convocations/")
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)
