from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from movie_website.settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apis.user_views.urls'),name='user_views'),
]


urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
