from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from movie_website.settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apis.user_apis.urls'),name='user_apis'),
    path('api/v1/', include('apis.movie_apis.urls'),name='movie_apis'),
    path('api/v1/', include('apis.relation_apis.urls'),name='relation_apis'),
    path('api/v1/', include('apis.interaction_apis.urls'),name='interaction_apis'),
]


urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
