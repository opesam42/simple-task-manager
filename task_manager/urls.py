from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tasks.urls', namespace='tasks')),
    path('users/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),

    path("components/", include("django_components.urls")),
]
