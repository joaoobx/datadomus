# Generated by Django 4.0 on 2024-05-21 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condominiumdocuments',
            name='doc_url',
            field=models.FileField(blank=True, null=True, upload_to='cond_docs/'),
        ),
        migrations.AlterField(
            model_name='userdocuments',
            name='doc_url',
            field=models.FileField(blank=True, null=True, upload_to='cond_docs/'),
        ),
    ]