from django.urls import path,include
from django.contrib import admin
from apps.categories.views import CategoryAPIView,CategoryCreateAPIView,CategoryDeleteAPIView,CategoryUpdateAPIView

urlpatterns = [
    #category api
    path('admin/',admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/categories',CategoryAPIView.as_view(),name = "category_api"),
    path('api/category/create',CategoryCreateAPIView.as_view(),name = "category_create_api"),
    path('api/category/update/<int:pk>',CategoryUpdateAPIView.as_view(),name = "category_api_update"),
    path('api/category/delete/<int:pk>',CategoryDeleteAPIView.as_view(),name = "category_api_delete"),
]   