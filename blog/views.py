# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    # template_name = 'blog/index.html'
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

# Create your views here.
# FBV 방법
# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts' : posts,
#         }
#     )

# def single_post_page(request, pk):

# pk=pk -> 데이터베이스 안에 키를 딱 하나 찍어서 가져온다 는 것
#     post = Post.objects.get(pk=pk)

#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post' : post,
#         }
#     )