from . import views
from django.urls import path

urlpatterns = [
    path('', views.TabList.as_view(), name='home'),
    path('bookmarked_tabs/', views.bookmarked_tabs, name='bookmarked_tabs'),
    path('search/', views.search_tabs, name='search_tabs'),
    path('toggle_bookmark/<int:tab_id>/', views.toggle_bookmark, name='toggle_bookmark'),
    path('<slug:slug>/edit_review/<int:review_id>/', views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>', views.review_delete, name='review_delete'),
    path('<slug:slug>/', views.tab_detail, name='tab_detail'),
]
