# Generated by Django 4.1.5 on 2023-01-15 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_request_starting_point_request_cycle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cycle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
