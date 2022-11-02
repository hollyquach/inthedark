from django.urls import path, include
from .views import toptracks

urlpatterns = [
    path('toptracks/', toptracks, name="toptracks"),
]