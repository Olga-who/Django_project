from django.shortcuts import get_list_or_404, render
from django.core.paginator import Paginator

from goods.models import Products
from goods.utils import q_search


def catalog(request, category_slug=None):

    on_sale = request.GET.get("on_sale", None)
    order_by = request.GET.get("order_by", None)
    page = request.GET.get("page", 1)
    query = request.GET.get("q", None)

    if category_slug == "all":
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))
    context = {
        "titel": "Home - Каталог",
        "goods": current_page,
        "category_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {"product": product}
    return render(request, "goods/product.html", context)
