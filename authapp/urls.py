from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'user_profile', UserProfileView, basename='user-profile'),
router.register(r'profile', ProfileView, basename='profile')


urlpatterns = [
    path(
        "me/",
        MeView.as_view(),
        name="me"
    ),   
]

urlpatterns += router.urls