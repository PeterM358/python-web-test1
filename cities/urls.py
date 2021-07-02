from django.urls import path

from djangoStart.cities.views import index

urlpatterns = [
    path('', index)
]