# Generated by Django 5.1.4 on 2025-01-01 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_joblocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='contactEmail',
            field=models.EmailField(default='', max_length=200, null=True),
        ),
    ]
