from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# genre for all movies
class Genre(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name

# types of languages
class Language(models.Model):
    lang = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.lang

# main movie model for all pages
class Movie(models.Model):
    pic = models.ImageField()
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=600)
    # many to many used for giving it to many movies
    genre = models.ManyToManyField(Genre)
    date_of_release = models.DateField()
    languages = models.ManyToManyField(Language)
    
    def __str__(self):
        return str(self.name)
    
# Display for my list for evry user
class MyList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch = models.BooleanField(default=False)