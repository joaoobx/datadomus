from django.db import models

class SugestionBoard(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    doc_url  = models.FileField(null=False, blank=False, upload_to="sugestion_boards/")
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)

class EventBoard(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    doc_url  = models.FileField(null=False, blank=False, upload_to="event_boards/")
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)

class NoticeBoard(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    doc_url  = models.FileField(null=False, blank=False, upload_to="notice_boards/")
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)

class UsefulPhonesBoard(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    doc_url  = models.FileField(null=False, blank=False, upload_to="useful_phones_boards/")
    created_at = models.DateTimeField(auto_now_add=True, max_length=100, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, max_length=100)
    deleted_at = models.DateTimeField(null=True)
