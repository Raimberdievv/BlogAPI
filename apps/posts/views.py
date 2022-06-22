from rest_framework import generics
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer,PostCreateSerializer,PostUpdateSerializer

class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

class PostUpdateAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer