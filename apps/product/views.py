from django.urls import reverse
from django.http import JsonResponse, HttpResponseRedirect, \
    HttpResponse, HttpResponseForbidden

from apps.product.models import Product
from apps.product.form import ProductForm


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