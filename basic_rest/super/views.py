from rest_framework import viewsets

from .serializers import HeroSerializer, MovieSerializer, PublisherSerializer
from .models import Hero, Movie, Publisher


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class MovielViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('publisher','release_date')
    serializer_class = MovieSerializer

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('name')
    serializer_class = PublisherSerializer