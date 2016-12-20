from encodings.idna import nameprep

from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from .models import *
from .forms import UserLoginForm, UserRegistrationForm, DealForm

def auth_login(request):
    loginform = UserLoginForm(request.POST or None)
    registrationform = UserRegistrationForm(request.POST or None)
    if loginform.is_valid():
        username = loginform.cleaned_data.get('username')
        password = loginform.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
    if registrationform.is_valid():
        user =registrationform.save(commit=False)
        password = registrationform.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        login(request, user)
    if request.user.is_authenticated:
        return redirect(home)
    return render(request, 'login.html', {"loginform": loginform, "registrationform": registrationform})

def auth_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    towar = Product.objects.order_by('views')[:10]
    return render(request, 'home.html', {"towar": towar})

def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {"categories": categories})

def tovar_list(request, category_name):
    categories = Category.objects.filter(name=category_name.title())
    if categories.exists():
        items = Product.objects.filter(category=categories)
        return render(request, 'content.html', {'items': items})
    else:
        return redirect(category)

def towar_info(request, category_name, towar_id):
    towar=Product.objects.get(pk=towar_id)
    loginform = UserLoginForm(request.POST or None)
    buyform = DealForm(request.POST or None)
    if loginform.is_valid():
        username = loginform.cleaned_data.get('username')
        password = loginform.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
    if buyform.is_valid():
        user = request.user
        adress=buyform.cleaned_data.get('adress')
        telephone =buyform.cleaned_data.get('telephone')
        deal = Deal(user=user, adress=adress,telephone=telephone,status='Accepted',product=towar)
        deal.save()
        return redirect(home)
    if request.user.is_authenticated:
        return render(request, 'item_info.html', {"loginform": loginform,"buyform": buyform, 'towar': towar})
    return render(request, 'item_info.html', {"loginform": loginform, "buyform": buyform, 'towar': towar})