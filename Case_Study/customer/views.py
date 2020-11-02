from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def home(request):
    context = {}
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('Email')
            address = form.cleaned_data.get('Address')
            contact = form.cleaned_data.get('Contact')
            date = form.cleaned_data.get('Date')
            password= form.cleaned_data.get('password1')
            p=Customer(Name=username,Address=address,Email=email,Contact=contact,Status=False,Password=password,Date=date)
            p.save()
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def customer_details(request):
    context={
    'customer_details' : Customer.objects.all()
    }
    return render(request,'customer_details.html',context)
