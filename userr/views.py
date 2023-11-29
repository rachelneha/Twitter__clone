from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm,TweetForm
from django.views.generic import CreateView, DetailView, ListView, FormView, UpdateView, View
from .models import User, Tweets
from django.contrib.auth import authenticate, login as django_login
from django.urls import reverse_lazy


# Create your views here.


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            django_login(request, form.user)
            return redirect('/home/?login-success')
    else:
        form = LoginForm()
    return render(request, "login.html", {'form': form})


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = "signup.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        user.set_password(form.cleaned_data['password'])
        user.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        authenticated_user = authenticate(self.request,username=username, password=password)
        if authenticated_user:
            django_login(self.request, authenticated_user)
            return super().form_valid(form=form)
        else:
            return render(self.request, "signup.html")



class HomeView(CreateView):
    model = Tweets
    template_name = "home.html"
    context_object_name = "tweets"
    form_class = TweetForm
    success_url = reverse_lazy('home')