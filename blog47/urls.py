
from django.contrib import admin
from django.urls import path
from posts.views import html_view, posts_list_view, main_view, posts_detail_view, create_post_view
from django.conf.urls.static import static
from django.conf import settings
from user.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name="main-page"),
    path('html/', html_view),
    path('posts/', posts_list_view),
    path('posts/<int:id>/', posts_detail_view),
    path('posts/create/', create_post_view),
    path('register/', register_view),
    path('login/', login_view, name="login-view" ),
    path('logout/', logout_view, name="logout-view"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) 