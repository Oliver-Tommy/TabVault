from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):

    def test_form_is_valid(self):
        review_form = ReviewForm({'rating': 5, 'comment': 'Post is valid'})
        self.assertTrue(review_form.is_valid())