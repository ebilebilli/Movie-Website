from django.urls import path

from apis.relation_apis.category_views import *


app_name = 'relation_apis'

urlpatterns = [
    path(
        'categories/', 
        CategoryListAPIView.as_view(), 
        name='categories'
        ),
    path(
        'category/<int:category_id>/movies/', 
        MoviesByCategoriesAPIView.as_view(), 
        name='movies-by-category'
        )  
]