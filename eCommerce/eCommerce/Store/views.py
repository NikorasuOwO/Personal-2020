from Store.models import Product
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from . import forms
from django.db.models import Q 
# Create your views here.

def redirect_store(request, *args, **kargs):
    return redirect(store)

def store(request):

    if request.method == 'POST':

        # ORDER
        if request.POST.get('order')[0] == 'n': # NUMERICALLY
            if request.POST.get('order')[1] == 'a':
                products = Product.objects.order_by('price')
            else: products = Product.objects.order_by('-price')
        else:
            if request.POST.get('order')[1] == 'a': # ALPHABETICALLY
                products = Product.objects.order_by('name')
            else: products = Product.objects.order_by('-name')

        #CONTAINS COLOR
        products = Product.objects.filter(color1=request.POST.get('color')).union(Product.objects.filter(color2=request.POST.get('color')))
        filter_form = forms.FilterForm(request.POST)
    else:
        products = Product.objects.order_by('name')
        filter_form = forms.FilterForm()

    context = {"products":products, "number":products.count()}

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