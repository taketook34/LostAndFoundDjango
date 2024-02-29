from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('postlist/', PostList.as_view(), name='postlist'),
    path('contacts/', contacts, name="contacts"),
    path('postlist/<int:post_id>/', PostShow.as_view(), name="post"),
    path('registration/', register_page, name="register"),
    path('logout/', logout_page, name="logout"),
    path('login/', login_page, name='login'),
    path('addpost/', add_post, name="addpost"),
    path('postlist/<int:post_id>/comment/', add_comment, name="addcomment")
]