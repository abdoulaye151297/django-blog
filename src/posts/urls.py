from django.urls import path
from .views import HomeView, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete

app_name = "posts"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', BlogPostCreate.as_view(), name='create'),
    path('<str:slug>/', BlogPostDetail.as_view(), name='detail'),
    path('<str:slug>/edit/', BlogPostUpdate.as_view(), name='edit'),
    path('<str:slug>/delete/', BlogPostDelete.as_view(), name='delete'),
]
