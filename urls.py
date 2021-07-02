from django.contrib import admin
from django.urls import path, include

# from djangoStart.views import index
from djangoStart.cities.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include('djangoStart.cities.urls')),
    path('', index),  # от тук взима индекс хтмл
]
