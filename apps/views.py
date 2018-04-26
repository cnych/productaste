# -*- coding: utf-8 -*-
from django.shortcuts import render

from apps.product.models import Product

from utils.time_utils import date


def index_view(request):
    products_dict = dict()
    for i in range(3):
        _date = date(-i).date()
        products_dict[_date.strftime('%Y-%m-%d')] = Product.objects.filter(
            public=True, created_at__contains=_date).\
            order_by('-vote_count', '-created_at')
    # products = Product.objects.filter(public=True).order_by('-vote_count', '-created_at')
    context = {
        'products_dict': products_dict
    }
    return render(request, 'index.html', context)
