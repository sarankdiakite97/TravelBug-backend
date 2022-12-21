from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include('apps.categories.urls')),
    path('places/', include('apps.places.urls')),
]
