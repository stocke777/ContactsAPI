from .models import Tweet
from rest_framework.serializers import ModelSerializer


class TweetSerializer(ModelSerializer):

    class Meta:
        model = Tweet
        fields = ['id', 'author', 'content']