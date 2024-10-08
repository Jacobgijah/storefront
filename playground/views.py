from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product, OrderItem, Order

def say_hello(request):
    # product = Product.objects.filter(pk=0).exists()
    # try:
    #     product = Product.objects.filter(pk=0)
    # except ObjectDoesNotExist:
    #     pass
    
    ######## dealing with filters
    # keyword=value
    # queryset = Product.objects.filter(description__isnull=True)
    
    ######## complex lookups using Q objetcs
    # Products: inventory < 10 and unit_price < 20
    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # queryset = Product.objects.filter(inventory__lt=10).filter(unit_price__lt=20)
    # Products: inventory < 10 or unit_price < 20
    # queryset = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    
    ####### sorting
    # queryset = Product.objects.order_by('unit_price', '-title')
    # product = Product.objects.order_by('-unit_price')[0]
    # product = Product.objects.earliest('-unit_price')
    
    ####### limiting results
    # 0, 1, 2, 3, 4
    # queryset = Product.objects.all()[:5]
    
    ####### selecting fields to query
    # queryset = Product.objects.values('id', 'title', 'collection__title')
    # queryset = Product.objects.values_list('id', 'title', 'collection__title')
    # select ordered products and sort them by title
    # queryset = Product.objects.filter(
    #     id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    
    ####### deferring fields
    # only method should be used wisely as it send a lot number of queries to a DB
    # queryset = Product.objects.only('id', 'title')
    
    # selecting related objects
    # select_related(1)
    # queryset = Product.objects.select_related('collection').all()
    # prefetch_related(n)
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    
    queryset = Order.objects.select_related(
        'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    
    return render(request, 'hello.html', {'name': 'Jeco', 'orders': list(queryset)})
