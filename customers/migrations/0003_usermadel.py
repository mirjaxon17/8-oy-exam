# Generated by Django 5.0.6 on 2024-06-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_rename_full_name_teleusers_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMadel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.TextField(null=True)),
                ('is_staff', models.BooleanField(default=False, null=True)),
                ('telegram_id', models.PositiveBigIntegerField(unique=True, verbose_name='Telegram Id')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
