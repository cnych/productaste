from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden

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
