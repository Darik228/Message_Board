from django.shortcuts import render
from django.urls import reverse_lazy
from .models import NewUser
from .serializers import NewUserSerializer
from rest_framework import viewsets
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView


class NewUserViewSet(viewsets.ModelViewSet):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer


def index(request):
    queryset = NewUser.objects.all()
    return render(request, template_name='registr/index.html', context={'queryset': queryset})


class LoginUser(LoginView):
    form_class = LoginForm
    template_name = "registr/login.html"

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterForm
    template_name = "registr/register.html"

    def get_success_url(self):
        return reverse_lazy('home')
