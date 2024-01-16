from django.urls import path
from .views import LoginPageView, logout_user, signUpView, home, PostView


urlpatterns = [
    path('signup/', signUpView.as_view(), name='signUpView'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
    path('createpost/', PostView.as_view(), name='createpost'),
]