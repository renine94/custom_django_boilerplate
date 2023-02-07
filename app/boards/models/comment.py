from django.db import models

from core.base.models import BaseDateTime
from app.boards.models import Article


class CommentManager(models.Manager):
    """defind Custom Method"""

    def get_by_article(self, query: Article):
        """게시글로 댓글을 가져온다."""
        return self.filter(article=query)


class CommentQuerySet(models.QuerySet):
    """define Filter & Annotation"""

    def annotate_content_length(self):
        """댓글 길이 계산"""
        return self.annotate(content_length=Count('content'))

    def filter_content_length_gte(self, query):
        """댓글 길이가 query 이상 값 리턴"""
        return self.annotate_content_length().filter(content_length__gte=query)


class Comment(BaseDateTime, models.Model):
    class Meta:
        verbose_name_plural = '댓글'

    def __str__(self):
        return self.content

    objects = CommentManager.from_queryset(CommentQuerySet)()

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='comments', verbose_name='댓글 작성자')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments', verbose_name='댓글 게시글')

    content = models.TextField(verbose_name='댓글 내용')
