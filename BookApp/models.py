from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name

class Translator(models.Model):
    name=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    def __str__(self):
        return self.name


class Rating(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    grade=models.IntegerField()
    comment=models.TextField()
    date=models.DateField()
    def __str__(self):
        return f"{self.user.username} Rating: {self.grade}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    date_added = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_of_pages = models.IntegerField()
    image=models.ImageField(upload_to='book_images')
    availability=models.BooleanField()
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}{self.author}"

class BookRating(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    rating=models.ForeignKey(Rating, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title}{self.rating}"


class BookTranslator(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    translator=models.ForeignKey(Translator,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.book.title}{self.translator.name}"



