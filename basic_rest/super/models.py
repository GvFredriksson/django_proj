from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Publisher(models.Model):
    name = models.CharField(max_length=60)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    def __str__(self):
        return self.name
    

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=60)
    hero = models.ForeignKey(Hero, null=True ,on_delete=models.CASCADE, related_name='hero')
    villain = models.ForeignKey(Hero, null=True, on_delete=models.CASCADE, related_name='villain')
    release_date = models.DateField(blank=True)
    score = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name