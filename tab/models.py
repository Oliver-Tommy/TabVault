from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg

def validate_pdf_file(value):
    if not value:
        raise ValidationError('A PDF file is required')
    if not str(value).lower().endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed')


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
    file = CloudinaryField('pdf', validators=[validate_pdf_file])
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
    
    def clean(self):
        super().clean()
        if not self.file:
            raise ValidationError({'file': 'A PDF file is required'})
        
        if not str(self.file).lower().endswith('.pdf'):
            raise ValidationError({'file': 'File must be a PDF'})

    @property
    def average_rating(self):
        return self.reviews.aggregate(Avg('rating'))['rating__avg'] or 0
        
    @property
    def review_count(self):
        return self.reviews.count()


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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = CloudinaryField('image', default='placeholder')
    website = models.URLField(max_length=200, blank=True)
    social_links = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
