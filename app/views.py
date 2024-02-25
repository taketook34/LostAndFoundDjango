from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView


def home(request):

    return render(request, 'app/homepage.html', {'page_title': 'Головна сторінка'})
    
#assets/

# def postlist(request):
#     context = {
#         'posts': Post.objects.all(),
#         'page_title': 'Знахідки'
#     }

#     return render(request, 'app/postlist.html', context=context)

class PostList(ListView):
    model = Post
    template_name = "app/postlist.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Знахідки'
        return context

    def get_queryset(self):
        return Post.objects.all()
    

def contacts(request):
    context = {
        "authors": [
            {"name":"Хусаінов Дмитро ІО-11"},
            {"name":"Шинкарчук Богдан ІО-11"},
            {"name":"Столярчук Микола ІО-11"}
        ],
        'page_title': 'Про нас' 

    }

    return render(request, 'app/contacts.html', context=context)
    

# def show_post(request, post_id):
#     """ ЕНдпоінт для кожної сторінки"""
#     post = get_object_or_404(Post, id=post_id)

#     return render(request, "app/showpost.html", context={'post': post, 'page_title': f'Пост \"{post.name}\"'})

class PostShow(DetailView):
    model = Post
    template_name = 'app/showpost.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Пост'
        return context

    def get_object(self):
        return Post.objects.get(pk=self.kwargs['post_id'])


def register_page(request):

    return render(request, "app/registerpage.html", {'page_title': 'Реєстрація'})

def login_page(request):

    return render(request, "app/loginpage.html", {'page_title': 'Логін'})


