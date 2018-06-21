from django.contrib import admin

from apps.comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'product', 'is_ban', 'add_time',)
    list_filter = ('is_ban',)


admin.site.register(Comment, CommentAdmin)
