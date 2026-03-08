"""URL configuration for edustream project."""

from django.contrib import admin
from django.urls import path

from edustream.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
