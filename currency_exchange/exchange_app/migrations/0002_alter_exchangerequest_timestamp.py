# Generated by Django 5.0.1 on 2024-01-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerequest',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
