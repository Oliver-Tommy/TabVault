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

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    file = CloudinaryField('pdf', default='placeholder')
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='tabs')
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    bookmarks = models.ManyToManyField(User, related_name="bookmarked_tabs",
                                        blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} by {self.artist}"


class Review(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE,
                            related_name="reviews")
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Review by {self.user.username} for {self.tab.title}"
