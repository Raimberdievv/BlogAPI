from dataclasses import field
from rest_framework import serializers
from apps.posts.models import Post,PostComment

#Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

#PostComment
class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = "__all__"

class PostCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = "__all__"

class PostCommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = "__all__"