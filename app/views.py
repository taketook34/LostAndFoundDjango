from django.shortcuts import render
from .models import Post, Comment


def home(request):
    
    return render(request, 'app/homepage.html')
    
#assets/

def postlist(request):
    context = {
        'posts': Post.objects.all(),
        # 'posts': [
        #     {"title": "Заголовок 1", "description": "Опис 1", "number": 1},
        #     {"title": "Заголовок 2", "description": "Опис 2", "number": 2},
        # ]
    }

    return render(request, 'app/postlist.html', context=context)
    

def contacts(request):
    context = {
        "authors": [
            {"name":"Хусаінов Дмитро ІО-11"},
            {"name":"Шинкарчук Богдан ІО-11"},
            {"name":"Столярчук Микола ІО-11"}
        ] 

    }

    return render(request, 'app/contacts.html', context=context)
    

def show_post(request, post_id):
    """ ЕНдпоінт для кожної сторінки"""

    return render(request, "app/showpost.html", context={'number': post_id})


def register_page(request):

    return render(request, "app/registerpage.html")

def login_page(request):

    return render(request, "app/loginpage.html")


