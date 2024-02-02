from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


class News(models.Model):
    image = models.ImageField(upload_to='news_images', blank=True)
    title = models.CharField(max_length=128, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = "News"


class Comment(models.Model):
    nick_name = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    news = models.ForeignKey('News', null=True, blank=True, on_delete=models.CASCADE)
    count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'Comment by {self.nick_name} on {self.date}'

    def like(self):
        self.likes += 1
        self.save()

    def dislike(self):
        self.dislikes += 1
        self.save()


@receiver(post_save, sender=Comment)
def update_comment_count(sender, instance, **kwargs):
    news = instance.news
    if news:
        news.comment_count = Comment.objects.filter(news=news).count()
        news.save()
