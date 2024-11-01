from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from users.forms import CustomUserCreationForm

# Create your views here.
def register(request):

    form = CustomUserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Welcome {username}, your account is created')

        return redirect('login')

    return render(request, 'users/register.html', {'form': form})


@login_required
def profilepage(request):
    return render(request, "users/profile.html")
