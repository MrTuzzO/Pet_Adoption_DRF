from rest_framework import serializers
from .models import Dog


class DogSerializer(serializers.ModelSerializer):
    color_names = serializers.SerializerMethodField()
    author_username = serializers.CharField(source='author.username', read_only=True)  # Display the author's username

    class Meta:
        model = Dog
        exclude = ['author']

    def get_color_names(self, obj):
        return [color.name for color in obj.colors.all()]

    def create(self, validated_data):
        colors_data = validated_data.pop('colors')
        request = self.context.get('request')  # Access the request object from the context
        validated_data['author'] = request.user  # Automatically set the author field
        dog = Dog.objects.create(**validated_data)
        dog.colors.set(colors_data)  # Set colors using their IDs
        return dog

    def update(self, instance, validated_data):
        # Handle optional image fields
        for image_field in ['image_1', 'image_2', 'image_3', 'image_4']:
            if image_field in validated_data:
                if validated_data[image_field] is not None:
                    setattr(instance, image_field, validated_data[image_field])
            else:
                # If the field is not provided, skip updating it
                validated_data.pop(image_field, None)

        # Handle optional colors
        colors_data = validated_data.pop('colors', None)
        if colors_data is not None:
            instance.colors.set(colors_data)

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
