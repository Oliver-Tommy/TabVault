from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Tab

# Create your views here.

class TabList(generic.ListView):
    model = Tab
    template_name = "tab/index.html"
    paginate_by = 6

def tab_detail(request, slug):
    """
    Display an individual :model:`tab.Tab`.

    **Context**

    ``tab``
        An instance of :model:`tab.Tab`.

    **Template:**

    :template:`tab/tab_detail.html`
    """

    queryset = Tab.objects
    tab = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "tab/tab_detail.html",
        {"tab": tab},
    )