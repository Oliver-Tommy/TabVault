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

    title = models.CharField(max_length=100, unique=True)         # Tab title
    slug = models.SlugField(max_length=100, unique=True)         # Slug field
    artist = models.CharField(max_length=100)        # Artist name
    genre = models.CharField(max_length=50)          # Genre of the music
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)  # Difficulty level
    file = CloudinaryField('pdf', default='placeholder')    # Uploaded file (PDF or text)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tabs')  # Link to the creator
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-filled timestamp
    views = models.IntegerField(default=0)          # Track the number of views

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Review(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]  # Ratings from 1 to 5 stars

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who left the review
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE)    # Link to the tab being reviewed
    rating = models.IntegerField(choices=RATING_CHOICES)        # Star rating
    comment = models.TextField(blank=True)                      # Optional comment
    created_at = models.DateTimeField(auto_now_add=True)        # Timestamp for when the review was submitted

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Review by {self.user.username} for {self.tab.title}"
