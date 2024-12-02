from django.urls import path
from .views import HomePageView

app_name = 'feed'

# class based views
urlpatterns = [
    path('', HomePageView.as_view(), name='post_list'),
]