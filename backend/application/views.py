# for serializer
from application.models import User
from rest_framework import generics
from application.serializer import UserSerializer

# for signup function
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# serializer registration
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# another one
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
