from django.contrib import admin
from django.urls import path
from .views import home  # import your home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # map the root URL to your home view
]