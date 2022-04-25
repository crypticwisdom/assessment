from django.contrib.auth.models import User
from rest_framework import serializers

from post.models import Post


class Owner(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'email', 'is_staff']


class PostCreationSerializer(serializers.ModelSerializer):
    owner = Owner()

    class Meta:
        model = Post
        fields = ['owner', 'slug', 'title', 'content']


# Post and Likes
class PostListSerializer(serializers.ModelSerializer):
    owner = Owner()

    class Meta:
        model = Post
        fields = ['owner', 'likes', 'likes_count', 'title', 'slug', 'published']


