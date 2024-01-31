from django.urls import path

from news.views import HomePageView, NewsDetailView, add_comment, LikeCommentView, DislikeCommentView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/add_comment/', add_comment, name='add_comment'),
    path('comment/<int:comment_id>/like/', LikeCommentView.as_view(), name='like_comment'),
    path('comment/<int:comment_id>/dislike/', DislikeCommentView.as_view(), name='dislike_comment'),
]
