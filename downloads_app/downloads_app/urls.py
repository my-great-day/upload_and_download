from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from download_app import views

router = routers.DefaultRouter()
router.register(r'create_the_file', views.FileUploadCreateAPIView, basename='create_the_file')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('download_app.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
