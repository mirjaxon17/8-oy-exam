# Generated by Django 5.0.6 on 2024-06-17 08:54

import django.db.models.deletion
import shop.helpers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=shop.helpers.SaveMediaFiles.category_img_path)),
                ('create_date', models.DateField(auto_now=True)),
                ('last_update', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('full_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=shop.helpers.SaveMediaFiles.testiminial_img_path)),
                ('create_date', models.DateField(auto_now=True)),
                ('last_update', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=shop.helpers.SaveMediaFiles.product_img_path)),
                ('price', models.FloatField()),
                ('price_type', models.CharField(choices=[('$', 'USD'), ('UZS', "so'm")], default='$', max_length=10)),
                ('create_date', models.DateField(auto_now=True)),
                ('last_update', models.DateField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField(auto_now=True)),
                ('last_update', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
        ),
    ]