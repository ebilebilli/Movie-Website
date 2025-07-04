from django.urls import path

from apis.interaction_apis.bookmark_views import *


app_name = 'bookmark_apis'

urlpatterns = [
    # Bookmark endpoints
    path(
        'bookmarks/', 
        BookmarkListAPIView.as_view(), 
        name='bookmarks'
        ),
    path(
        'movie/<slug:slug>/bookmark/', 
        AddBookmarkAPIView.as_view(), 
        name='post-bookmark'
        ),
    path(
        'bookmark/<int:bookmark_id>/', 
        DeleteBookmarkAPIView.as_view(), 
        name='delete-bookmark'
        )  
]