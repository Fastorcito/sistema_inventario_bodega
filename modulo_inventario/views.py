from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Product, Inventory, Location
from .forms import ProductForm, ProductUpdateForm
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST['username']
            password = request.POST['password1']
            try:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)
                print("hey")
                return redirect('index')
            except IntegrityError:
                return render(request, "users/signup.html", {
                    'form': UserCreationForm(),
                    'error': "El nombre de usuario ya existe"
                }) 
        else:
            return render(request, "users/signup.html", {
                'form': UserCreationForm(),
                'error': "Las contraseñas no coinciden"
            }) 
    else:
        return render(request, "users/signup.html", {
            'form': UserCreationForm()
        })

def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("hey")
            return redirect('index')
        else:
            return render(request, "users/signin.html", {
                'form': AuthenticationForm(),
                'error': "Nombre de usuario o contraseña incorrecta"
            })
    else:
        return render(request, "users/signin.html", {
            'form': AuthenticationForm()
        })

def index(request):
    return render(request, "index.html")

@login_required
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

@login_required
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

@login_required
def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('products_list')

@login_required
def inventory_menu(request):
    locations = Location.objects.all()
    return render(request, 'inventories/inventories_menu.html', {'locations':locations} )

@login_required
def inventory_list(request, inventory_id):
    location = get_object_or_404(Location, id=inventory_id)
    inventories = Inventory.objects.filter(location=location)
    return render(request, 'inventories/inventories_list.html', {'location': location, 'inventories': inventories})

@login_required
def add_quantity(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        inventory.quantity += quantity
        inventory.save()
    return redirect('inventories_list', location_id=inventory.location.id)

@login_required
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

