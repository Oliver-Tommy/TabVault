from . import views
from django.urls import path

urlpatterns = [
    path('', views.TabList.as_view(), name='home'),
    path('<slug:slug>/', views.tab_detail, name='tab_detail'),
    path('<slug:slug>/edit_review/<int:review_id>/', views.review_edit, name='review_edit'),
]
