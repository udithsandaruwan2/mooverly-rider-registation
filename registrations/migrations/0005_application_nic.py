# Generated by Django 5.1.4 on 2024-12-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0004_remove_application_nic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='nic',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]