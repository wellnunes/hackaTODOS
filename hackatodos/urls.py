from django.contrib import admin
from django.urls import path

from hackatodos.views import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
