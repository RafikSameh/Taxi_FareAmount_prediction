from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('ModelAPI.urls')),
    path('admin/', admin.site.urls),
]
