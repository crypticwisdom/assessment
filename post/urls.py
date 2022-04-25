from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('create/', views.PostCRUD.as_view(), name="create"),
    path('delete/<slug:slug>/', views.PostCRUD.as_view(), name="delete"),
    path('update/<slug:slug>/', views.PostCRUD.as_view(), name="update"),
    path('like/<slug:slug>/', views.LikePost.as_view(), name="like"),
    path('list/', views.PostList.as_view(), name="list")

]