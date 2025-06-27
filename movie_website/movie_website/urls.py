from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from movie_website.settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),

    # Google Sign-In urls
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/social/', include('allauth.socialaccount.urls')),
]


urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
