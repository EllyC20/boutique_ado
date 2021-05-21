from django.shortcuts import render
from .models import Product


def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    """ A view to show all products, including sorting and searching """
    return render(request, 'products/products.html', context)
