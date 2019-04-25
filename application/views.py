# for serializer
from django.http import HttpResponse

from .models import User
from rest_framework import generics
from .serializer import UserSerializer

# for signup function
from django.shortcuts import render, redirect



# serializer registragion
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# another one


def show_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('pass')
        user = User(email=email, name=name, password=password)
        user.save()
        return HttpResponse('200')

    return render(request, 'application/signup.html')



