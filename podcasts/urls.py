from django.urls import path

from .views import HomePageView, new_feed

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('new_feed/', new_feed, name="new_feed")
]