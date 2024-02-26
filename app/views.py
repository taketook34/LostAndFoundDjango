from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Comment

from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import redirect_to_login


def home(request):

    return render(request, 'app/homepage.html', {'page_title': 'Головна сторінка'})
    
#assets/

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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect_to_login(request.GET.get('next'), request.META['HTTP_REFERER'])
    else:
        form = UserCreationForm()
    return render(request, "app/registerpage.html", {'page_title': 'Реєстрація', 'form':form})

def logout_page(request):

    logout(request)
    return redirect('home')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "app/loginpage.html", {'page_title': 'Логін', 'error_message':'Нерпавильний логін або пароль'})
    else:
        return render(request, "app/loginpage.html", {'page_title': 'Логін'})


