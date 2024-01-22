from django.urls import path
from .views import LoginPageView, logout_user, signUpView,LikePostView, home, PostView, PostListView, CommentCreateView



urlpatterns = [
    path('signup/', signUpView.as_view(), name='signup'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('home/', PostListView.as_view(), name='home'),
    path('createpost/', PostView.as_view(), name='createpost'),
    path('create_comment/<int:post_id>/', CommentCreateView.as_view(), name='createcomment'),
]
