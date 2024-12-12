
from django.contrib import admin
from django.urls import path
from posts.views import html_view, posts_list_view, main_view, posts_detail_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', main_view),
    path('html/', html_view),
    path('posts/', posts_list_view),
    path('detail/', posts_detail_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) 