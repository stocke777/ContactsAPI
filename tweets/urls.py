

from django.urls import path, include
from .views import TweetList

urlpatterns = [
    path('', TweetList.as_view()),
]