from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.http import HttpResponseRedirect

def post_list(request):
    try:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})
    except Exception as e:
        return render(request, 'blog/error.html', {'error': str(e)})

def post_detail(request, pk):
    try:
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})
    except Exception as e:
        return render(request, 'blog/error.html', {'error': str(e)})

@login_required
def post_new(request):
    try:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                # Проверяем, что пользователь аутентифицирован
                if request.user.is_authenticated:
                    post.author = request.user
                    post.published_date = timezone.now()
                    post.save()
                    return redirect('post_detail', pk=post.pk)
                else:
                    # Перенаправляем на страницу входа
                    return HttpResponseRedirect('/admin/login/?next=/post/new/')
        else:
            form = PostForm()
        
        return render(request, 'blog/post_edit.html', {'form': form})
    except Exception as e:
        return render(request, 'blog/error.html', {'error': str(e)})