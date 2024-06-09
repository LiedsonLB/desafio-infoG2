from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SurvivorViewSet

router = DefaultRouter()
router.register(r'survivors', SurvivorViewSet, basename='survivor')

urlpatterns = [
    path('', include(router.urls)),
]