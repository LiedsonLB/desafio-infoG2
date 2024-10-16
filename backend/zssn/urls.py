from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from api.views import SurvivorViewSet

router = DefaultRouter()
router.register(r'survivors', SurvivorViewSet, basename='survivor')

def index(request):
    return HttpResponse("Bem-vindo ao meu site Django!")

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]