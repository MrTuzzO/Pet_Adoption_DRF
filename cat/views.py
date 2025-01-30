import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from accounts.permission import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Cat, CatColor
from .serializers import CatSerializer, ColorSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

class PetPagination(PageNumberPagination):
    page_size = 18


# class CatFilter(django_filters.FilterSet):
#     gender = django_filters.CharFilter(field_name='gender', lookup_expr='iexact')  # Case-insensitive match
#
#     color = django_filters.CharFilter(
#         field_name='colors__name',  # Filtering by the 'name' of the 'colors' ManyToManyField
#         lookup_expr='iexact',  # Case-insensitive exact match
#     )
#
#     class Meta:
#         model = Cat
#         fields = ['gender', 'color']

# Or operation in color-------and with gender
class CatFilter(django_filters.FilterSet):
    gender = django_filters.CharFilter(field_name='gender', lookup_expr='iexact')

    color = django_filters.CharFilter(method='filter_colors')

    def filter_colors(self, queryset, name, value):
        # Split the colors by comma or spaces for multiple values
        colors = self.request.query_params.getlist('color')
        if colors:
            query = Q()
            for color in colors:
                query |= Q(colors__name__iexact=color)
            return queryset.filter(query).distinct()
        return queryset

    class Meta:
        model = Cat
        fields = ['gender', 'color']


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    pagination_class = PetPagination  # If you have pagination setup
    filter_backends = [DjangoFilterBackend]
    filterset_class = CatFilter  # Use your custom filter class

    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]  # Adjust permissions as needed

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ColorViewSet(ModelViewSet):
    queryset = CatColor.objects.all()
    serializer_class = ColorSerializer