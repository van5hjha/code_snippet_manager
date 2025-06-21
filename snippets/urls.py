from rest_framework.routers import DefaultRouter
from .views import SnippetViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('', SnippetViewSet, basename='snippets')

urlpatterns = [
    path('', include(router.urls)),
]
