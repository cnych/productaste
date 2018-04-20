from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.account.models import MyUser
from utils.id_utils import hashid


class Product(models.Model):
    pid = models.CharField(max_length=32, unique=True, editable=False, verbose_name='产品ID')
    name = models.CharField(max_length=100, verbose_name='名称')
    url = models.URLField(verbose_name='产品链接')
    digest = models.CharField(max_length=200, verbose_name='一句话描述')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='用户')
    vote_count = models.IntegerField(default=0, verbose_name='点赞数')
    public = models.BooleanField(default=True, verbose_name='上线?')
    remark = models.CharField(max_length=200, default='', blank=True,
                              null=True, verbose_name='备注')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name = '产品'
        verbose_name_plural = '产品管理'

    def __str__(self):
        return '%s(%s)' % (self.name, self.pid)


class ProductVote(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    add_time = models.IntegerField(default=0)

    class Meta:
        db_table = 'product_vote'
        verbose_name = '产品点赞'
        verbose_name_plural = '产品点赞'


@receiver(post_save, sender=Product, dispatch_uid='gen_product_pid')
def update_uid(sender, instance, **kwargs):
    if not instance.pid:
        instance.pid = hashid(instance.id, length=8)  # 生成产品UID
        instance.save()
