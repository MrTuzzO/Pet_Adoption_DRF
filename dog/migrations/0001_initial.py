# Generated by Django 5.1.5 on 2025-01-26 17:21

import django.db.models.deletion
import pet.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cat', '0001_initial'),
        ('pet', '0002_remove_pet_age_pet_month_pet_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('pet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pet.pet')),
                ('food_habit', models.TextField()),
                ('breed', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('Tiny', 'Tiny (<5kg)'), ('Small', 'Small (5-10kg)'), ('Medium', 'Medium (10-25kg)'), ('Large', 'Large (25-45kg)'), ('Giant', 'Giant (>45kg)')], max_length=50)),
                ('description', models.TextField()),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='pet_images/cat_img/', validators=[pet.models.validate_image])),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='pet_images/cat_img/', validators=[pet.models.validate_image])),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='pet_images/cat_img/', validators=[pet.models.validate_image])),
                ('colors', models.ManyToManyField(related_name='dogs', to='cat.catcolor')),
            ],
            bases=('pet.pet',),
        ),
    ]
