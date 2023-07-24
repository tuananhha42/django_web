from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Customer
from django.core.cache import caches
from django.core.cache import cache
from django.core.cache.backends.base import InvalidCacheBackendError
# Create your views here.
from django.views.decorators.cache import cache_page
# @cache_page(60 * 15)
def listing(request):
    try:
        customer_list = caches["customer_list"]
    except InvalidCacheBackendError:
        customer_list = Customer.objects.all()
        caches["customer_list"] = customer_list

    print('cache:', caches['customer_list'])

    paginator = Paginator(customer_list,5)

    pageNumber = request.GET.get('page')
    try:
        customers = paginator.page(pageNumber)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, 'pagination_1.html', {'customers':customers}) 
# trỏ thẻ html sau cùng, ở đây pagiation_1 nó bao gồm cả list.html nên trỏ pagination_1, 
# ngoai ra co the tro den pagination_2 hoac pagination_3