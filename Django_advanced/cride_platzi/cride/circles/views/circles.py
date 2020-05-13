"""Circle views."""

# Django REST Framewrok
from rest_framework import viewsets

# serializers
from cride.circles.serializers import CircleModelSerializer

# Models
from cride.circles.models import Circle


class CircleViewSet(viewsets.ModelViewSet):
    "Circle view set. """

    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer