from django.shortcuts import render, get_object_or_404
from .models import Product
from factory1.models import Product as Factory1Product
from factory2.models import Product as Factory2Product

def product_list(request):
    factory1_products = Factory1Product.objects.all()
    factory2_products = Factory2Product.objects.all()
    return render(request, 'product_list.html', {
        'factory1_products': factory1_products,
        'factory2_products': factory2_products
    })


def product_detail(request, product_id):
    product = get_object_or_404(ConfectioneryFactoryproduct2, id=product_id)
    return render(request, 'product_detail.html', context={'product': product})
