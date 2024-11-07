# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# Vista para la página de inicio
def home(request):
    return render(request, 'home.html')  # Asegúrate de tener esta plantilla creada

def register_admin(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Asegúrate de que 'home' esté definido en tus URLs
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Asegúrate de que 'home' esté definido en tus URLs
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def admin_dashboard(request):
    return render(request, 'accounts/dashboard.html')  # Asegúrate de crear este template
