from django.db import models

from core.base.models import BaseModel


class ArticleManager(models.Manager):
    pass


class ArticleQuerySet(models.QuerySet):
    pass


class Article(BaseModel, models.Model):
    class Meta:
        verbose_name_plural = '게시글'

    def __str__(self):
        return self.title

    objects = ArticleManager.from_queryset(ArticleQuerySet)()

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='articles', verbose_name='게시글 작성자')

    title = models.CharField(max_length=120, verbose_name='게시글 제목')
    content = models.TextField(verbose_name='게시글 내용')
    like_count = models.PositiveIntegerField(default=0, verbose_name='추천 수')
