from rest_framework import generics
from apps.posts.models import Post,PostComment
from apps.posts.serializers import PostCommentCreateSerializer, PostCommentSerializer, PostCommentUpdateSerializer, PostSerializer,PostCreateSerializer,PostUpdateSerializer

#Post
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

#PostComment
class PostCommentAPIView(generics.ListAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

class PostCommentCreateAPIView(generics.ListAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentCreateSerializer

class POstCommentUpdateAPIView(generics.ListAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentUpdateSerializer

class PostCommentDeleteAPIView(generics.DestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer     