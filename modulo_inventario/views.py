from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, Inventory, Location
from .forms import ProductForm, ProductUpdateForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def product_list(request):
    products = Product.objects.all()
    form = ProductForm()
    context = {'products': products, 'form': form}
    return render(request, 'products/product_list.html', context)

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductForm()
    products = Product.objects.all()
    context = {'products': products, 'form': form}
    return render(request, 'products/product_list.html', context)

def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_list')
    else:
        form = ProductUpdateForm(instance=product)
    
    context = {'form': form, 'product_id': product_id}

    return render(request, 'products/product_update.html',context)

def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('products_list')