from django.urls import path
from . import views
from userr.views import SignupView,HomeView


urlpatterns = [
    path("", views.login, name="login"),
    path("signup/", SignupView.as_view(),name="signup"),
    path("home/", HomeView.as_view(),name="home"),
]