from django.shortcuts import render, get_object_or_404
from .models import Post

def render_posts(request):
    post = Post.objects.all()
    return render(request, 'post.html', {'post': post})

def post_detail(request, post_id):
    post_id = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {"post":post_id})