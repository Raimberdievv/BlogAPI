from django.urls import path,include
from django.contrib import admin
from apps.posts.views import PostAPIView,PostCreateAPIView,PostUpdateAPIView,PostDeleteAPIView

urlpatterns = [
    #post api
    path('admin/',admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/post',PostAPIView.as_view(),name = "post_api"),
    path('api/post/create',PostCreateAPIView.as_view(),name = "post_create_api"),
    path('api/post/update/<int:pk>',PostUpdateAPIView.as_view(),name = "post_api_update"),
    path('api/post/delete/<int:pk>',PostDeleteAPIView.as_view(),name = "post_api_delete"),
]  