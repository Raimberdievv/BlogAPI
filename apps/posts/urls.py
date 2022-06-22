from django.urls import path,include
from django.contrib import admin
from apps.posts.views import PostAPIView,PostCreateAPIView,PostUpdateAPIView,PostDeleteAPIView
from apps.posts.views import PostCommentAPIView,PostCommentCreateAPIView,POstCommentUpdateAPIView,PostCommentDeleteAPIView

urlpatterns = [
    #post api
    path('admin/',admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/post',PostAPIView.as_view(),name = "post_api"),
    path('api/post/create',PostCreateAPIView.as_view(),name = "post_create_api"),
    path('api/post/update/<int:pk>',PostUpdateAPIView.as_view(),name = "post_api_update"),
    path('api/post/delete/<int:pk>',PostDeleteAPIView.as_view(),name = "post_api_delete"),

    #postcomment api
    path('admin/',admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/post_comment',PostCommentAPIView.as_view(),name = "post_comment_api"),
    path('api/post_comment/create',PostCommentCreateAPIView.as_view(),name = "post_comment_create_api"),
    path('api/post_comment/update/<int:pk>',POstCommentUpdateAPIView.as_view(),name = "post_comment_api_update"),
    path('api/post_comment/delete/<int:pk>',PostCommentDeleteAPIView.as_view(),name = "post_comment_api_delete"),
]  