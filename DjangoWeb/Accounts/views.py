from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login,logout
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from django.views.generic import CreateView
from . import forms
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
