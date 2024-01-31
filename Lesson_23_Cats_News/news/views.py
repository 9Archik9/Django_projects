from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView

from news.forms import CommentForm
from news.models import News, Comment


class HomePageView(View):
    news = News.objects.all().order_by('date')

    def get(self, request):
        return render(request, 'news.html', context={'news': self.news})


class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['all_comments'] = Comment.objects.filter(news=self.object)
        return context


def add_comment(request, pk):
    if request.method == 'POST':
        news = get_object_or_404(News, pk=pk)
        form = CommentForm(request.POST)
        # all_comments = Comment.objects.filter(news=news)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            parent_comment_id = request.POST.get('parent_comment_id')

            if parent_comment_id:
                parent_comment = get_object_or_404(Comment, pk=parent_comment_id)
                comment.parent_comment = parent_comment
                comment.save()

                parent_comment.replies.add(comment)
                parent_comment.save()

            else:
                comment.save()

    return redirect('news_detail', pk=pk)


class LikeCommentView(View):
    def post(self, request, comment_id):
        comment = Comment.objects.get(pk=comment_id)
        comment.likes += 1
        comment.save()
        return JsonResponse({'likes': comment.likes, 'dislikes': comment.dislikes})


class DislikeCommentView(View):
    def post(self, request, comment_id):
        comment = Comment.objects.get(pk=comment_id)
        comment.dislikes += 1
        comment.save()
        return JsonResponse({'likes': comment.likes, 'dislikes': comment.dislikes})
