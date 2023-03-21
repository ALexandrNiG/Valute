from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import RegForm
from .models import Applicant


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'userapp/login.html'


class UserCreateView(CreateView):
    model = Applicant
    template_name = 'userapp/register.html'
    form_class = RegForm
    success_url = reverse_lazy('users:login')
