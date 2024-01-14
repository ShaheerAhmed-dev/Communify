from django.urls import path
from django.contrib.auth.views import LoginView
from .views import UserRegistrationView, home, PostView



urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='UserRegistrationView'),
    path('login/', LoginView.as_view(), name='login'),
    path('home/', home, name='home'),
    path('createpost/', PostView.as_view(), name='createpost'),
]