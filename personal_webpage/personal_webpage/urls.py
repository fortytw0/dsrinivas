from django.contrib import admin
from django.urls import path
from .views import front_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , front_page)
]
