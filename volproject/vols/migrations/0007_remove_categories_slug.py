# Generated by Django 4.0.4 on 2022-05-20 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vols', '0006_categories_delete_latest_categories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='slug',
        ),
    ]
