# Generated by Django 5.0.6 on 2024-10-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0010_dtmresult_chosen_variant_dtmresult_true_variant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dtmresult',
            name='chosen_variant',
        ),
        migrations.RemoveField(
            model_name='dtmresult',
            name='true_variant',
        ),
        migrations.AddField(
            model_name='answer',
            name='chosen_variant',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='true_variant',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
