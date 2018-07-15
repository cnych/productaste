from django.db import models

from apps.account.models import MyUser
from apps.product.models import Product
from apps.comment.manager import CommentManager


class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='用户')
    content = models.TextField(verbose_name='评论内容')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='所属产品')
    parent = models.ForeignKey('self', blank=True, null=True, 
        on_delete=models.CASCADE, verbose_name='所属评论')
    is_ban = models.BooleanField(default=False, verbose_name='禁言?')

    objects = CommentManager()
    
    class Meta:
        verbose_name = '评论管理'
        verbose_name_plural = verbose_name
        db_table = 'comment'
    
    def __str__(self):
        return self.content[:20]
    
    @property
    def replies(self):
        return Comment.objects.filter(is_ban=False, parent=self).order_by('-add_time')
    