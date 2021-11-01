from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet
from django.http import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .serializers import TweetSerializer


# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required()
def randomtweets(request):
    tweets = Tweet.objects.all()
    print(tweets)
    d = {}
    for tweet in tweets:
        d[tweet.id] = {
            'author': tweet.author,
            'content': tweet.content
        }
    return JsonResponse(d)

class TweetList(ListCreateAPIView):

    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    def get_queryset(self):
        return Tweet.objects.order_by('?')[:2]
