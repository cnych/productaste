from django.db.models import Manager


class CommentManager(Manager):
    def get_comments(self, product):
        """获取产品product的评论列表"""
        return self.filter(is_ban=False, parent__isnull=True, product=product).order_by('-add_time')

    def get_comment_count(self, product):
        return self.filter(is_ban=False, product=product).count()
        