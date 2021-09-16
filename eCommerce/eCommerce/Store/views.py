from Store.models import Product
from django.shortcuts import get_object_or_404, redirect, render
from . import forms

# Create your views here.

def redirect_store(request, *args, **kargs):
    return redirect(store)

def store(request):

    products = Product.objects.all()

    context = {"products":products, "number":products.count()}

    filter_form = forms.FilterForm()

    context["filter_form"] = filter_form

    return render(request, 'Store/store.html', context)

def view_prod(request, id):

    product = get_object_or_404(Product, id=id)

    context = {
        "name":product.name,
        "description":product.description,
        "price":product.price,
        "image":product.image,
        }

    return render(request, 'Store/product.html', context)