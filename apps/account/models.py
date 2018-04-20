from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save

from apps.account.const import GENDERS, GENDER_N
from utils.id_utils import hashid


class MyUser(AbstractUser):
    uid = models.CharField(max_length=32, unique=True, editable=False, verbose_name='用户ID')
    nickname = models.CharField(max_length=50, blank=True, null=True,
                                default='', verbose_name='昵称')
    gender = models.CharField(max_length=10, choices=GENDERS,
                              default=GENDER_N, verbose_name='性别')
    avatar = models.CharField(max_length=500,
                              default=settings.DEFAULT_AVATAR_URL, verbose_name='头像')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'myuser'
        verbose_name = '用户'
        verbose_name_plural = '用户管理'

    def __str__(self):
        return self.username


class GithubUser(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE,
                             blank=True, null=True)
    gid = models.CharField(max_length=50, editable=False)
    login = models.CharField(max_length=200)
    name = models.CharField(max_length=200, blank=True, null=True, default='')
    email = models.CharField(max_length=100, blank=True, null=True, default='')
    bio = models.CharField(max_length=200, blank=True, null=True, default='')
    location = models.CharField(max_length=200, blank=True, null=True, default='')
    repos_url = models.URLField()
    avatar_url = models.URLField()
    url = models.URLField()
    followers_url = models.URLField()
    subscriptions_url = models.URLField()
    html_url = models.URLField()
    organizations_url = models.URLField()
    public_gists = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    public_repos = models.IntegerField(default=0)
    created_at = models.CharField(max_length=20)
    updated_at = models.CharField(max_length=20)

    class Meta:
        db_table = 'github_user'
        verbose_name = 'Github用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.login


@receiver(post_save, sender=MyUser, dispatch_uid='gen_myuser_uid')
def update_uid(sender, instance, **kwargs):
    if not instance.uid:
        instance.uid = hashid(instance.id)  # 生成用户UID
        instance.save()