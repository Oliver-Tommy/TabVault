from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.db.models import Avg, Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Tab, Review
from .forms import ReviewForm


class TabList(generic.ListView):
    """
    Display a paginated list of all available :model:`tab.Tab`.

    **Context**

    ``tab_list``
        A queryset of all :model:`tab.Tab` instances, paginated.

    **Template:**

    :template:`tab/index.html`
    """

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

    ``average_rating``
        The average rating of all reviews for the tab.

    ``full_stars``
        The number of full stars to display in the rating.

    ``half_star``
        A boolean indicating whether to display a half-star.

    **Template:**

    :template:`tab/tab_detail.html`
    """
    tab = get_object_or_404(Tab, slug=slug)
    reviews = Review.objects.filter(tab=tab).order_by("-created_at")
    review_count = reviews.count()
    average_rating = reviews.aggregate(Avg("rating")).get("rating__avg") or 0
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
            messages.add_message(request, messages.SUCCESS,
                                 "Comment submitted")

    review_form = ReviewForm()
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


def review_edit(request, slug, review_id):
    """
    Edit an existing :model:`tab.Review`.

    **Context**

    ``tab``
        An instance of :model:`tab.Tab`.

    ``review``
        The :model:`tab.Review` instance being edited.

    ``review_form``
        A form instance pre-filled with the review data.

    **Redirect:**

    Redirects to the :view:`tab.tab_detail` view for the tab.
    """
    if request.method == "POST":
        tab = get_object_or_404(Tab, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.user == request.user:
            updated_review = review_form.save(commit=False)
            updated_review.tab = tab
            updated_review.save()
            messages.add_message(
                request, messages.SUCCESS, "Review updated successfully!"
            )
        else:
            messages.add_message(request, messages.ERROR,
                                 "Error updating review!")

    return HttpResponseRedirect(reverse("tab_detail", args=[slug]))


def review_delete(request, slug, review_id):
    """
    Delete an existing :model:`tab.Review`.

    **Context**

    ``tab``
        An instance of :model:`tab.Tab`.

    ``review``
        The :model:`tab.Review` instance being deleted.

    **Redirect:**

    Redirects to the :view:`tab.tab_detail` view for the tab.
    """
    tab = get_object_or_404(Tab, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.user == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, "Comment deleted!")
    else:
        messages.add_message(
            request, messages.ERROR, "You can only delete your own comments!"
        )

    return HttpResponseRedirect(reverse("tab_detail", args=[slug]))


def search_tabs(request):
    """
    Search for :model:`tab.Tab` instances based on user query.

    **Context**

    ``tabs``
        A queryset of :model:`tab.Tab` instances matching the query.

    ``query``
        The search string entered by the user.

    **Template:**

    :template:`tab/search_results.html`
    """
    query = request.GET.get("q", "")
    if query:
        tabs = Tab.objects.filter(
            Q(title__icontains=query)
            | Q(artist__icontains=query)
            | Q(genre__icontains=query)
        )
    else:
        tabs = Tab.objects.all()

    return render(request, "tab/search_results.html",
                  {"tabs": tabs, "query": query})


@login_required
def toggle_bookmark(request, tab_id):
    """
    Toggle the bookmark status of a :model:`tab.Tab` for the logged-in user.

    **Context**

    ``tab``
        The :model:`tab.Tab` being bookmarked or unbookmarked.

    **Redirect:**

    Redirects to the :view:`tab.tab_detail` view for the tab.
    """
    tab = get_object_or_404(Tab, id=tab_id)
    if request.method == "POST":
        if request.user in tab.bookmarks.all():
            tab.bookmarks.remove(request.user)
            messages.add_message(
                request, messages.SUCCESS, "Tab removed from bookmarks!"
            )
        else:
            tab.bookmarks.add(request.user)
            messages.add_message(request, messages.SUCCESS,
                                 "Tab added to bookmarks!")

    return redirect("tab_detail", slug=tab.slug)


@login_required
def bookmarked_tabs(request):
    """
    Display a list of tabs bookmarked by the logged-in user.

    **Context**

    ``bookmarks``
        A queryset of :model:`tab.Tab` instances bookmarked by the user.

    **Template:**

    :template:`tab/bookmarked_tabs.html`
    """
    bookmarks = request.user.bookmarked_tabs.all()
    return render(request, "tab/bookmarked_tabs.html",
                  {"bookmarks": bookmarks})
