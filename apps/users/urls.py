from django.urls import path,include
from django.contrib import admin
from apps.users.views import UserAPIView,UserCreateAPIView,UserDeleteAPIView,UserUpdateAPIView

urlpatterns = [
    #user api
    path('admin/',admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/user',UserAPIView.as_view(),name = "user_api"),
    path('api/user/create',UserCreateAPIView.as_view(),name = "user_create_api"),
    path('api/user/update/<int:pk>',UserDeleteAPIView.as_view(),name = "user_api_update"),
    path('api/user/delete/<int:pk>',UserUpdateAPIView.as_view(),name = "user_api_delete"),
]  