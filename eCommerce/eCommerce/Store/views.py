from Store.models import Product
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from . import forms
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def redirect_store(request, *args, **kargs):
    return redirect(store)

def store(request):

    if request.method == 'POST':
    
        filter_form = forms.FilterForm(request.POST)
        products = Product.objects.all()

        #PRICE IS BELOW
        #return HttpResponse(request.POST.get('price'))
        if request.POST.get('price_below'):
            products = products.filter(price__lte=request.POST.get('price_below'))

        #CONTAINS COLOR
        if request.POST.get('color') != "any":
            products = products.filter(Q(color1__iexact=request.POST.get('color')) | Q(color2__iexact=request.POST.get('color')))
    
        #TYPE OF SHOE
        if request.POST.get('type') != "any":
            products = products.filter(type=request.POST.get('type'))

        # ORDER
        if request.POST.get('order')[0] == 'n': # NUMERICALLY
            if request.POST.get('order')[1] == 'a':
                products = products.order_by('price')
            else: products = products.order_by('-price')
        else:
            if request.POST.get('order')[1] == 'a': # ALPHABETICALLY
                products = products.order_by('name')
            else: products = products.order_by('-name')

    else: # If no constraint
        products = Product.objects.order_by('name')
        filter_form = forms.FilterForm(initial={'type': 'any', 'color':'any'})

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

def login_view(request):
    context = {}
    formlog = User
    return render(request, 'Store/login.html', context)

def register_view(request):
    form = forms.CreateUserForm()

    if request.method == 'POST':
        form = forms.CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, 'Store/register.html', context)