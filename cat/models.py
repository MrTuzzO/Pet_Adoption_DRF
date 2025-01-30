from django.db import models
from pet.models import Pet, validate_image


class CatColor(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Cat(Pet):
    colors = models.ManyToManyField(CatColor, related_name="cats")
    food_habit = models.TextField()
    is_potty_trained = models.BooleanField(default=False)
    description = models.TextField()
    image_2 = models.ImageField(upload_to='pet_images/cat_img/', validators=[validate_image], blank=True, null=True)
    image_3 = models.ImageField(upload_to='pet_images/cat_img/', validators=[validate_image], blank=True, null=True)
    image_4 = models.ImageField(upload_to='pet_images/cat_img/', validators=[validate_image], blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.id}"