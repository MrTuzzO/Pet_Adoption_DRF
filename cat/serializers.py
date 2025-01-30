from rest_framework import serializers
from .models import Cat, CatColor


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatColor
        fields = ['id', 'name']


# class CatSerializer(serializers.ModelSerializer):
#     color_names = serializers.SerializerMethodField()
#     author_username = serializers.CharField(source='author.username', read_only=True)  # Display the author's username
#
#     class Meta:
#         model = Cat
#         exclude = ['author']
#
#     def get_color_names(self, obj):
#         # Return a list of color names related to the Cat instance
#         return [color.name for color in obj.colors.all()]
#
#     def create(self, validated_data):
#         colors_data = validated_data.pop('colors')
#         request = self.context.get('request')  # Access the request object from the context
#         validated_data['author'] = request.user  # Automatically set the author field
#         cat = Cat.objects.create(**validated_data)
#         cat.colors.set(colors_data)  # Set colors using their IDs
#         return cat
#
#     def update(self, instance, validated_data):
#         colors_data = validated_data.pop('colors')
#         instance.colors.set(colors_data)  # Update colors using their IDs
#         return super().update(instance, validated_data)


class CatSerializer(serializers.ModelSerializer):
    color_names = serializers.SerializerMethodField()
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Cat
        exclude = ['author']

    def get_color_names(self, obj):
        # Return a list of color names related to the Cat instance
        return [color.name for color in obj.colors.all()]

    def create(self, validated_data):
        # Extract colors data from validated_data
        colors_data = validated_data.pop('colors', None)
        request = self.context.get('request')  # Access the request object from the context
        validated_data['author'] = request.user  # Automatically set the author field
        cat = Cat.objects.create(**validated_data)  # Create the Cat instance

        if colors_data:
            cat.colors.set(colors_data)  # Associate colors if provided

        return cat

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
