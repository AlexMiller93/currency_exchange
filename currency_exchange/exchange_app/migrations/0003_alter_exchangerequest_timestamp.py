# Generated by Django 5.0.1 on 2024-01-25 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_app', '0002_alter_exchangerequest_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerequest',
            name='timestamp',
            field=models.DateField(auto_now=True),
        ),
    ]
