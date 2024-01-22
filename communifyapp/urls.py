from django.urls import path
from .views import LoginPageView, logout_user, home, CreatePostView, PostUpdateView, PostDeleteView, PostView, \
    CommentCreateView, profile, HomeView
from .views import EditProfileView, signUpView

urlpatterns = [
    path('signup/', signUpView.as_view(), name='signup'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('createpost/', CreatePostView.as_view(), name='createpost'),
    path('updatepost/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('deletepost/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/', PostView.as_view(), name='post'),
    path('commentpost/<int:pk>/', CommentCreateView.as_view(), name='comment-create'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', EditProfileView.as_view(), name='edit-profile'),
    # path('posttype/', PostTypeView.as_view(), name='posttype'),
]