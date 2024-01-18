from django.urls import path
from .views import LoginPageView, logout_user, signUpView, home, CreatePostView, PostUpdateView, PostDeleteView, PostView


urlpatterns = [
    path('signup/', signUpView.as_view(), name='signUpView'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', home, name='home'),
    path('createpost/', CreatePostView.as_view(), name='createpost'),
    path('updatepost/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('deletepost/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/', PostView.as_view(), name='post')
    # path('posttype/', PostTypeView.as_view(), name='posttype'),
]