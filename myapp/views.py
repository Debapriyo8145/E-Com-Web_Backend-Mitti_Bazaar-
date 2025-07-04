from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Products

def index(request):
    
    products = Products.objects.all()[:6]  
    return render(request, 'myapp/index.html', {'products': products})
    

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, "Password didn't matched !!...")
        
            return redirect ('signup')
    
        elif User.objects.filter(username = username).exists():
            messages.error(request, "This User Name is Alredy taken!!...")
        
            return redirect ('signup')
        
        user = User.objects.create_user(username = username, email = email, password = password)
        user.save()

        messages.success(request, "Congratulations Your Account has been created succesfully!!")
        return redirect('account')

    return render(request,'myapp/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)                                               #main function for login
            messages.success(request, "Welcome Back")
            return redirect('/')
        
        elif request.user.is_authenticated:
            return redirect('account')
        
        else:
            messages.error(request, "Login Failed !!!")
            return redirect('login')
        
    return render(request,'myapp/login.html')

def logout_view(request):
    logout(request)
    messages.success(request,"You are succesfully logedout...")
    return redirect('index')


@login_required
def account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        
    return render(request,'myapp/account.html')

@login_required
def wishlist(request):
    return render(request,'myapp/wishlist.html')

def about(request):
    return render(request,'myapp/about.html')

@login_required
def cart(request):
    return render(request,'myapp/cart.html')

@login_required
def order_history(request):
    return render(request,'myapp/order_his.html')

def shop(request):
    products = Products.objects.all()
    
    return render(request,'myapp/shop.html', {'products':products})

def product_details(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    related_products = Products.objects.filter(category=product.category).exclude(id=product.id)[:6]
    
    return render(request,'myapp/product_details.html', {'product':product, 'related_products':related_products})

def cart_view(request):
    cart = request.session.get('cart',{})
    products = Products.objects.filter(id__in = cart.keys())
    
    cart_items = []
    total = 0
    
    for product in  products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        total += subtotal
        total_pieces = product.quantity * quantity
        
        cart_items.append({
            'product':product,
            'quantity':quantity,
            'subtotal':subtotal,
            'total_pieces':total_pieces
        })
    
    return render (request, 'myapp/cart.html', {'cart_items':cart_items, 'total':total})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    
    return redirect('cart_view')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
        
    return redirect('cart_view')

from django.shortcuts import redirect

def update_cart(request):
    if request.method == 'POST':
        cart = request.session.get('cart', {})

        for key, value in request.POST.items():
            if key.startswith('quantities_'):
                product_id = key.split('_')[1]
                try:
                    quantity = int(value)
                    if quantity > 0:
                        cart[product_id] = quantity
                    else:
                        cart.pop(product_id, None)
                except ValueError:
                    continue

        request.session['cart'] = cart

    return redirect('cart_view')
