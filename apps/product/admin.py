from django.contrib import admin

from apps.account.models import MyUser
from apps.product.models import Product


class ProductAdmin(admin.ModelAdmin):
    # fields = ('name', 'url', 'digest', 'user', 'public', 'remark',)
    list_display = ('pid', 'name', 'digest', 'user', 'public',)
    search_fields = ('name', 'digest',)
    list_filter = ('public',)
    fieldsets = (
        ['Main', {
            'fields': ('name', 'url', 'digest'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # css
            'fields': ('user', 'public', 'remark'),
        }]
    )

admin.site.register(Product, ProductAdmin)
