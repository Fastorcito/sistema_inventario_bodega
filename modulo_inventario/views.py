from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product, Inventory, Location
from .forms import ProductForm

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
            return redirect('products/product_list')
    else:
        form = ProductForm()
    products = Product.objects.all()
    context = {'products': products, 'form': form}
    return render(request, 'products/product_list.html', context)

# def product_edit(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('products/product_list')
#     else:
#         form = ProductForm(instance=product)
#     products = Product.objects.all()
#     context = {'products': products, 'form': form}
#     return render(request, 'products/product_list.html', context)

# def product_delete(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('product_list')
#     products = Product.objects.all()
#     form = ProductForm()
#     context = {'products': products, 'form': form, 'product_to_delete': product}
#     return render(request, 'products/product_list.html', context)