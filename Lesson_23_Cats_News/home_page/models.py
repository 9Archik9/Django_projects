from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to='news_images', blank=True)
    title = models.CharField(max_length=128, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    comments = models.TextField(blank=True, null=True, default=None)

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

    def __str__(self):
        return f'Comment by {self.nick_name} on {self.date}'
