from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.db.models import Avg
from .models import Tab, Review
from .forms import ReviewForm

# Create your views here.

class TabList(generic.ListView):
    model = Tab
    template_name = "tab/index.html"
    paginate_by = 6

def tab_detail(request, slug):
    """
    Display an individual :model:`tab.Tab` with associated reviews.

    **Context**

    ``tab``
        An instance of :model:`tab.Tab`.

    ``reviews``
        A queryset of associated :model:`tab.Review` for the tab.

    ``review_count``
        The total number of reviews for the tab.

    **Template:**

    :template:`tab/tab_detail.html`
    """

    # queryset = Tab.objects
    tab = get_object_or_404(Tab, slug=slug)
    reviews = Review.objects.filter(tab=tab).order_by("-created_at")
    review_count = reviews.count()

    average_rating = reviews.aggregate(Avg('rating')).get('rating__avg') or 0
    full_stars = int(average_rating)
    half_star = (average_rating - full_stars) >= 0.5  

    url = tab.file.url.replace("http", "https")

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.tab = tab
            review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted'
            )

    review_form = ReviewForm()

    # increment view count
    tab.views += 1
    tab.save()

    return render(
        request,
        "tab/tab_detail.html",
        {
            "tab": tab,
            "reviews": reviews,
            "review_count": review_count,
            "review_form": review_form,
            "pdf": url,
            "average_rating": average_rating,
            "star_range": range(1, 6),
            "full_stars": full_stars,
            "half_star": half_star,
        },
    )
    