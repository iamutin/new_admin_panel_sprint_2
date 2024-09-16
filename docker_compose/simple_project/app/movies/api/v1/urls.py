from django.urls import path, include
from rest_framework import routers

from .views import MoviesViewSet

v1_router = routers.DefaultRouter()

v1_router.register('movies', MoviesViewSet, basename='movie')

urlpatterns = [
    path('', include(v1_router.urls)),
]
