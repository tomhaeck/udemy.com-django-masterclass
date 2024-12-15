from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

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


class PasswordChange(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('food:index')

    def form_valid(self, form):
        messages.success(self.request, "Your password was successfully changed.")
        return super().form_valid(form)
