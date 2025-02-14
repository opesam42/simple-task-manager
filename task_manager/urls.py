from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('tasks.urls', namespace='tasks')),
    path('users/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),

    path("components/", include("django_components.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)