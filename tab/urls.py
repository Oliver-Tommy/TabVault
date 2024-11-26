from . import views
from django.urls import path

urlpatterns = [
    path('', views.TabList.as_view(), name='home'),
    path('<slug:slug>/', views.tab_detail, name='tab_detail'),
]
