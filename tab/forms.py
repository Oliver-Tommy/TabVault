from django import forms
from .models import Review, UserProfile, Tab


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'website', 'social_links']
        widgets = {
            'social_links': forms.TextInput(attrs={'placeholder': 'Enter as JSON: {"twitter": "url", "instagram": "url"}'}),
        }


class TabForm(forms.ModelForm):
    class Meta:
        model = Tab
        fields = ['title', 'artist', 'genre', 'difficulty', 'file']
