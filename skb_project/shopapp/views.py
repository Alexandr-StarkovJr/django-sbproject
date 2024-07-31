from timeit import default_timer

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth.models import Group

def shop_index(request: HttpRequest):
    products = [
        ('Laptop', 1999),
        ('Desktop', 2000),
        ('Smartphone', 100),    
    ]
    
    context = {
        'time_running': round(default_timer(), 1),
        'products': products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)
