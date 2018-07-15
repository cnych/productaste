from django.urls import reverse
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, \
    HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from django.views.generic import View

from apps.product.models import Product
from apps.product.form import ProductForm
from apps.comment.form import CommentForm
from apps.comment.models import Comment


def new_product_view(request):
    if request.user.is_authenticated:
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('index'))

        return HttpResponse('<h1>产品分享失败~</h1>')

    else:
        return HttpResponseForbidden('<h1>未登录~</h1>')


def vote_product_view(request):
    pid = request.POST.get('pid', None)
    if pid is None:
        return JsonResponse({'errcode': 400, 'message': '参数错误'})
    
    if request.user is None or not request.user.is_authenticated:
        return JsonResponse({'errcode': 401, 'message': '未登录'})

    try:
        product = Product.objects.get(pid=pid)
        product.vote(request.user)
        return JsonResponse({'errcode': 200, 'message': '成功', 'data': {
            'vote_count': product.vote_count
        }})
        
    except Product.DoesNotExist:
        return JsonResponse({'errcode': 404, 'message': '产品不存在'})
    

def product_detail_view(request, pid):
    try:
        product = Product.objects.get(pid=pid)
        comments = Comment.objects.get_comments(product)
        comment_count =  Comment.objects.get_comment_count(product)
        context = {
            'product': product,
            'vote_users': product.get_vote_users(),
            'form': CommentForm,
            'comments': comments,
            'comment_count': comment_count
        }
        print(product.get_vote_users())
        return render(request, 'detail.html', context)
    except Product.DoesNotExist:
        return HttpResponseNotFound('产品不存在')



class ProductDetailView(View):
    methods = ['get', 'post']

    def get(self, request, pid):
        try:
            product = Product.objects.get(pid=pid)
            comments = Comment.objects.get_comments(product)
            comment_count =  Comment.objects.get_comment_count(product)
            context = {
                'product': product,
                'vote_users': product.get_vote_users(),
                'form': CommentForm,
                'comments': comments,
                'comment_count': comment_count
            }
            return render(request, 'detail.html', context)
        except Product.DoesNotExist:
            return HttpResponseNotFound('产品不存在')

    def post(self, request):
        pass
