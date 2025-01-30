from django.db import models
from pet.models import Pet, validate_image
from cat.models import CatColor


class Bird(Pet):
    SIZE_CHOICES = (
        ('Small', 'Small (<50g)'),
        ('Medium', 'Medium (50g-300g)'),
        ('Large', 'Large (>300g)'),
    )
    DIET_CHOICES = (
        ('Herbivore', 'Herbivore (Fruits, seeds, vegetables)'),
        ('Omnivore', 'Omnivore (Fruits, seeds, insects)'),
    )

    colors = models.ManyToManyField(CatColor, related_name="birds")
    species = models.CharField(max_length=100)
    food_habit = models.TextField()
    size = models.CharField(choices=SIZE_CHOICES, max_length=40)
    diet = models.CharField(choices=DIET_CHOICES, max_length=50)
    description = models.TextField()
    image_2 = models.ImageField(upload_to='pet_images/bird_img/', validators=[validate_image], blank=True, null=True)
    image_3 = models.ImageField(upload_to='pet_images/bird_img/', validators=[validate_image], blank=True, null=True)
    image_4 = models.ImageField(upload_to='pet_images/bird_img/', validators=[validate_image], blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.id}"