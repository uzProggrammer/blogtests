# Generated by Django 5.0.6 on 2024-09-21 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0002_adminlog_href'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminlog',
            name='type',
            field=models.CharField(choices=[('create', 'create'), ('update', 'update'), ('delete', 'delete')], default='create', max_length=255),
        ),
    ]
