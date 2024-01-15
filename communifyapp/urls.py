from django.urls import path
from .views import LoginPageView, logout_user
from .views import signUpView, home
from .models import CustomUser

urlpatterns = [
    path('signup/', signUpView.as_view(), name='signUpView'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home')
]