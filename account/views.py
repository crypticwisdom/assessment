from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


def home(request):
    print(request.__dir__(), request.get_host())
    return render(request, 'index.html')


class SignUpView(APIView):
    permission_classes = []

    def post(self, request):
        try:
            firstname = request.data.get('firstname')
            lastname = request.data.get('lastname')
            email = request.data.get('email')
            username = request.data.get('username')
            password = request.data.get('password')
            password_confirm = request.data.get("password_confirm")

            if not all([firstname, lastname, email, username, password, password_confirm]):
                return Response({"detail": "Please Provide firstname, lastname, email, username, password and password confirm"},
                                status=status.HTTP_400_BAD_REQUEST)

            if password != password_confirm:
                return Response({"detail": "Password Does not match"}, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create(
                first_name=firstname,
                last_name=lastname,
                email=email,
                username=username,
                password=make_password(password),
            )
            if user is not None:
                return Response({"detail": "Successfully created user", "access_token": AccessToken}, status=status.HTTP_200_OK)

            return Response({"detail": "Something Unexpected Happened"}, status=status.HTTP_400_BAD_REQUEST)
        except (Exception, ) as err:
            return Response({"detail": "An error occurred", "error": str(err)}, status=status.HTTP_400_BAD_REQUEST)
