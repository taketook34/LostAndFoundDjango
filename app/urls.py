from django.urls import path

from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('postlist/', postlist, name='postlist'),
    path('contacts/', contacts, name="contacts"),
    path('postlist/<int:post_id>/', show_post, name="showpost"),
    path('registration/', register_page, name="register"),
    path('login/', login_page, name='login')
]