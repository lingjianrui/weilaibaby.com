from django.db import models
from django.contrib.auth.models import AbstractUser
from markdownx.models import MarkdownxField


# Create your models here.
# 用户模型
class User(AbstractUser):
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username


# 文章模型
class Article(models.Model):
    user = models.ForeignKey(User, default=1, verbose_name='发布人')
    title = models.CharField(max_length=255, verbose_name='新闻标题')
    content = MarkdownxField(verbose_name='新闻内容')
    isMarkdown = models.BooleanField(default=1, verbose_name='Markdown?')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    isPublish = models.BooleanField(default=1, verbose_name='是否发布')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']
