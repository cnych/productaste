# -*- coding: utf-8 -*-
from datetime import timedelta
from django.shortcuts import render

from apps.product.models import Product

from utils.time_utils import date, str2date


def index_view(request):
    last_dt = request.GET.get('last_dt', None)
    if last_dt is None:  # 默认的首页
        products_dict = dict()
        for i in range(3):
            _date = date(-i).date()
            _key = _date.strftime('%Y-%m-%d')
            products_dict[_key] = Product.objects.filter(
                public=True, created_at__contains=_key).\
                order_by('-vote_count', '-created_at')
        context = {
            'products_dict': products_dict
        }
        return render(request, 'index.html', context)
    else:  # 渲染前一天的数据
        _date = str2date(last_dt) + timedelta(-1)
        _key = _date.strftime('%Y-%m-%d')
        context = {
            'date': _key,
            'products': Product.objects.filter(public=True, created_at__contains=_key).
                order_by('-vote_count', '-created_at')
        }
        return render(request, 'components/products.tpl.html', context)