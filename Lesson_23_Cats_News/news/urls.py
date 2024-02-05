from django.urls import path

from news.views import HomePageView, NewsDetailView, AddCommentView, LikeCommentView, DislikeCommentView, SortingNewsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('comment/<int:comment_id>/like/', LikeCommentView.as_view(), name='like_comment'),
    path('comment/<int:comment_id>/dislike/', DislikeCommentView.as_view(), name='dislike_comment'),
    path('sorting-news', SortingNewsView.as_view(), name='sorting-news'),
]
