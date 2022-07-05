from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views import View
from .models import *


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            m = Maqola.objects.get(user=request.user)
            return render(request, "home.html", {m:""})



class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        l = request.POST.get("log")
        p = request.POST.get("par")
        userlar = authenticate(request, username=l, password=p)
        if userlar is None:
            return redirect("login")
            login(request, userlar)
            return redirect("/home")



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")



class BlogView(View):
    def get(self, request):
        return redirect("blog.html")

    def post(self,request):
        a = request.POST.get("maqola")
        m = Maqola.objects.get(id=a)
        return redirect("maqola.html", {"sar":m})



class MaqolaView(View):
    def get(self, request):
        m1 = Maqola.objects.get()
        return render(request, "maqola.html")










