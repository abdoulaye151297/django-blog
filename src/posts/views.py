from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import BlogPost


class HomeView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'posts/home.html'


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = 'posts/posts_create.html'
    fields = ['title', 'content']


class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = 'posts/posts_edit.html'
    fields = ['title', 'content', 'author', 'created_on', 'published']


class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


class BlogPostDelete(DeleteView):
    model = BlogPost
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts:home')
    context_object_name = 'post'
