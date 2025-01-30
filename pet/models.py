from django.db import models
from rest_framework.exceptions import ValidationError
from accounts.models import CustomUser


def validate_image(image):
    max_size_mb = 5
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Image size cannot exceed {max_size_mb} MB.")


class Pet(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', 'Unknown'),
    )
    name = models.CharField(max_length=50)
    year = models.PositiveIntegerField(default=0)
    month = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    adoption_cost = models.PositiveIntegerField(default=0)
    adoption_status = models.BooleanField(default=False)
    location = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    image_1 = models.ImageField(upload_to='pet_images', validators=[validate_image], blank=False, null=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def get_pet_type(self):
        if hasattr(self, 'cat'):
            return 'cats'
        elif hasattr(self, 'dog'):
            return 'dogs'
        elif hasattr(self, 'bird'):
            return 'birds'
        return 'unknown'

    def __str__(self):
        return f"{self.name} - {self.id}"