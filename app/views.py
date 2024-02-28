from django.shortcuts import redirect, render, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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



# class AddPost(CreateView):
#     model = Post
#     template_name = 'app/addpost.html'
#     success_url = reverse_lazy('postlist')
#     login_url = reverse_lazy('login')
#     fields = ['name', 'description', 'photo', 'founder_contact']

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_title'] = 'Додати знахідку'
#         return context

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.save()
#         return super().form_valid(form)
    
#     def form_invalid(self, form):
#         context = self.get_context_data(form=form)
#         context['errors'] = form.errors
#         return self.render_to_response(context)

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    context = {
        'page_title': 'Додати пост',
        'form': form,
    }

    return render(request, 'app/addpost.html', context=context)


def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = Post.objects.get(pk=post_id)
            new_comment.save()
            return redirect('post', post_id=post_id)
    else:
        form = CommentForm()

    context = {
        'post_num': post_id,
        'page_title': 'Додати коментар',
        'form': form,
    }

    return render(request, 'app/addcomment.html', context=context)



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






