from django.urls import path
from . import views

# This is for the feeds post
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),

    # This class based view is being commented out because we are going to add new path
    # path('', views.PostListView.as_view(), name='post_list'),
    path('', views.post_list, name='post_list'),

    # This path is for the taggig view
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),

    path('feed/', LatestPostsFeed(), name='post_feed'),

    path('search/', views.post_search, name='post_search'),
]
