from django.db import models
from pet.models import Pet, validate_image
from cat.models import CatColor


class Dog(Pet):
    SIZE_CHOICES = (
        ('Tiny', 'Tiny (<5kg)'),
        ('Small', 'Small (5-10kg)'),
        ('Medium', 'Medium (10-25kg)'),
        ('Large', 'Large (25-45kg)'),
        ('Giant', 'Giant (>45kg)'),
    )
    colors = models.ManyToManyField(CatColor, related_name="dogs")
    food_habit = models.TextField()
    breed = models.CharField(max_length=50)
    size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    description = models.TextField()
    image_2 = models.ImageField(upload_to='pet_images/dog_img/', validators=[validate_image], blank=True, null=True)
    image_3 = models.ImageField(upload_to='pet_images/dog_img/', validators=[validate_image], blank=True, null=True)
    image_4 = models.ImageField(upload_to='pet_images/dog_img/', validators=[validate_image], blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.id}"