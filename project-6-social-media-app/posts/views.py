from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from posts.forms import PostCreateForm, CommentForm
from posts.models import Post

# Create your views here.
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST,
                              files=request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
    else:
        form = PostCreateForm()

    return render(request, 'posts/create.html', {'form': form})


def feed(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        new_comment = comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_comment.post = post
        new_comment.save()
    else:
        comment_form = CommentForm()

    posts = Post.objects.all()
    return render(request, 'posts/feed.html', {'posts': posts,
                                                                    'comment_form': comment_form})


def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('feed')





