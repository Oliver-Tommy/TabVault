from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Tab(models.Model):
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Intermediate', 'Intermediate'),
        ('Hard', 'Hard'),
    ]

    title = models.CharField(max_length=100)         # Tab title
    artist = models.CharField(max_length=100)        # Artist name
    genre = models.CharField(max_length=50)          # Genre of the music
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)  # Difficulty level
    file = CloudinaryField('pdf', default='placeholder')    # Uploaded file (PDF or text)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tabs')  # Link to the creator
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-filled timestamp
    views = models.IntegerField(default=0)          # Track the number of views

    def __str__(self):
        return f"{self.title} by {self.artist}"

