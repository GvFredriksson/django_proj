from rest_framework import serializers
from .models import Hero, Movie, Publisher

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = ('name', 'alias')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('name' ,'hero', 'villain', 'release_date', 'score','publisher')

class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ('name', 'start_date', 'end_date')