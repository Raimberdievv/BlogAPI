"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from apps.posts.views import PostAPIView,PostCreateAPIView,PostDeleteAPIView,PostUpdateAPIView

api_urlpatterns = [
    path('', include('apps.posts.urls')),
    path('', include('apps.users.urls')),
    path('', include('apps.categories.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    # path('api/', include(api_urlpatterns)),
    path('api/post',PostAPIView.as_view(),name = "post_api"),
    path('api/post/create',PostCreateAPIView.as_view(),name = "post_create_api"),
    path('api/post/update/<int:pk>',PostUpdateAPIView.as_view(),name = "post_api_update"),
    path('api/post/delete/<int:pk>',PostDeleteAPIView.as_view(),name = "post_api_delete"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)