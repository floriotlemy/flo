from django.shortcuts import render, redirect
from .form import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def inscription(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'formateur/inscription.html', {'form':form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'formateur/connexion.html')

@login_required
def accueil(request):
    return render(request, 'formateur/acceuil.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')