from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lesite.urls')),
    path('formateur/', include('formateur.urls')),
    path('compte/', include('compte.urls')),
]
