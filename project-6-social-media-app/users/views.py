from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from users.forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from users.models import Profile
from posts.models import Post

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # authenticate returns a user object if username and password are matched in database
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('User authenticated and logged in')
            else:
                return HttpResponse('Invalid credentials.  User could not be authenticated.')

    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def index(request):
    posts = Post.objects.filter(user=request.user)
    profile = Profile.objects.filter(user=request.user).first()
    return render(request,
                  'users/index.html',
                  {'posts': posts, 'profile': profile})


def register(request):

    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'users/register_done.html')
    else:
        user_form = UserRegistrationForm()

    return render(request, 'users/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'users/edit.html', {'user_form': user_form,
                                                                    'profile_form': profile_form})
