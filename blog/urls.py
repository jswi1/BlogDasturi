from django.contrib import admin
from django.urls import path

from app1.views import HomeView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
