from django.contrib import admin
from django.urls import path, include
from account.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', home, name="home"),
    path('post/', include('post.urls')),
    path('account/', include('account.urls')),
]
