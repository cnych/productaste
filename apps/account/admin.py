from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.account.models import MyUser, GithubUser
from apps.product.models import Product


class ProductInline(admin.TabularInline):
    model = Product


class MyUserAdmin(admin.ModelAdmin):
    def avatar_view(self, obj):
        html_tag = """<div style="width:100px;"><img width=100 src="%s"></div>""" % obj.avatar
        return mark_safe(html_tag)
    avatar_view.short_description = '头像'

    inlines = [ProductInline]  # inline
    list_display = ('uid', 'username', 'nickname', 'avatar_view', 'is_active', 'is_staff',)


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(GithubUser)
