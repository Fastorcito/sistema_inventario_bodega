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

def inventory_menu(request):
    locations = Location.objects.all()
    return render(request, 'inventories/inventories_menu.html', {'locations':locations} )

def inventory_list(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    inventories = Inventory.objects.filter(location=location)
    return render(request, 'inventories/inventories_list.html', {'location': location, 'inventories': inventories})

def add_quantity(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        inventory.quantity += quantity
        inventory.save()
    return redirect('inventories_list', location_id=inventory.location.id)

def reduce_quantity(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if inventory.quantity > quantity:
            inventory.quantity -= quantity
        else:
            inventory.quantity = 0
        inventory.save()
    return redirect('inventories_list', location_id=inventory.location.id)
