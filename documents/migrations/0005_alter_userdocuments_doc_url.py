# Generated by Django 4.0 on 2024-05-22 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_alter_condominiumdocuments_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdocuments',
            name='doc_url',
            field=models.FileField(blank=True, null=True, upload_to='user_docs/'),
        ),
    ]
