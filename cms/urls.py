from django.urls import path, include
from .views import main
from django.contrib import admin

urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
]