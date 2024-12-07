from django.urls import path
from .views import HomePageView, FeedPageView

app_name = 'feed'

# class based views
urlpatterns = [
    path('', HomePageView.as_view(), name='post_list'),
    path('feed', FeedPageView.as_view(), name='post_list'),
]