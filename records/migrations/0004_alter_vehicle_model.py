# Generated by Django 5.0.6 on 2024-05-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_alter_vehicle_status_alter_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='model',
            field=models.CharField(max_length=100),
        ),
    ]