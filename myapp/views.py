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
    
    return render(request,'myapp/product_details.html', {'product':product})



