from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect

from apps.product.models import Product
from apps.comment.models import Comment
from apps.comment.form import CommentForm


def new_comment_view(request):
    if request.user and request.user.is_authenticated:
        pid = request.POST.get('pid', None)
        rid = request.POST.get('rid', '0')

        try:
            product = Product.objects.get(pid=pid)
        except Product.DoesNotExist:
            return HttpResponseNotFound('产品不存在')
        
        if rid != '0':
            try:
                parent = Comment.objects.get(id=int(rid))
            except Comment.DoesNotExist:
                return HttpResponseNotFound('评论不存在')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            if rid != '0':
                comment.parent = parent
            comment.save()
            return HttpResponseRedirect(reverse('product-detail', kwargs={'pid': pid}))
        
        return HttpResponse('评论失败')

    else:
        return HttpResponseForbidden('未登录')
