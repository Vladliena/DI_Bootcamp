from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator,MinValueValidator,MinLengthValidator

class Book(models.Model):
    title = models.CharField(max_length=200,blank=False)
    author = models.CharField(max_length=50, blank=False)
    published_date = models.DateField(blank=False)
    description = models.TextField(blank=False)
    page_count = models.PositiveIntegerField()
    categories = models.CharField(max_length=50,blank=False)
    thumbnail_url = models.URLField(null=True)
    
    
class BookReview(models.Model):
    associated_book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    rating = models.PositiveIntegerField(default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
        )
    review_text = models.TextField(
        validators=[
            MinLengthValidator(10)
            ]
        )
    
    
    
    
    