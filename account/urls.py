from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name="sign-up"),
]
