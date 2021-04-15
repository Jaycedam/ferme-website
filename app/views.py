from django.shortcuts import render
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Persona

# Create your views here.

def admin(request):
    return render(request, '/admin/')

def home(request):
    return render(request, 'app/home.html')

def profile(request):
    current_user = request.user
    persona = Persona.objects.get(usuario=current_user.id)

    data = {
        "persona":persona,
        "user":current_user
    }

    return render(request, 'app/profile.html', data)

def register(request):
    data = {
        'form': CustomUserCreationForm(),
        'profile_form': UserProfileForm()
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if form.is_valid() and profile_form.is_valid():
            usuario = form.save()
            profile = profile_form.save(commit=False)

            profile.usuario = usuario

            profile.save()

            user = authenticate(username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"]
            )
            login(request, user)
            return redirect(to="home")
        data["form"] = form
        data["profile_form"] = profile_form

    return render(request, 'registration/register.html', data)