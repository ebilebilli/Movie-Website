from django.urls import path

from apis.interaction_apis.bookmark_views import *
from apis.interaction_apis.comment_views import *
from apis.interaction_apis.like_views import *


app_name = 'interaction_apis'

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
        name='movie-add-bookmark'
        ),
    path(
        'bookmark/<int:bookmark_id>/', 
        DeleteBookmarkAPIView.as_view(), 
        name='movie-delete-bookmark'
        ),
    # Comment endpoints
    path(
        'movie/<slug:slug>/comments/', 
        CommentListByMovieAPIView.as_view(), 
        name='comments'
        ),
    path(
        'movie/<slug:slug>/comment/', 
        AddCommentAPIView.as_view(), 
        name='movie-add-comment'
        ),
    path(
        'comment/<int:comment_id>/', 
        CommentDetailAPIView.as_view(), 
        name='comment-detail'
        ),
    path(
        'comment/<int:comment_id>/like', 
        AddLikeAPIView.as_view(), 
        name='comment-add-like'
        ),
    path(
        'like/<int:like_id>/', 
        DeleteLikeAPIView.as_view(), 
        name='comment-delete-like'
        ),
]