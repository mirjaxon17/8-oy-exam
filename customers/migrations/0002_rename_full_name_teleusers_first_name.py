# Generated by Django 5.0.6 on 2024-06-18 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teleusers',
            old_name='full_name',
            new_name='first_name',
        ),
    ]