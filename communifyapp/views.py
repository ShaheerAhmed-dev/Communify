from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from requests import post

from .models import CustomUser, Post, Profile
from .forms import SignupForm, PostForm, LoginForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View, ListView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


class signUpView(CreateView):
    model = CustomUser
    form_class = SignupForm
    template_name = 'communifyapp/signup.html'
    success_url = reverse_lazy('login')

    # def form_valid(self, form):
    #     print(form.errors)
    #     response = super().form_valid(form)
    #     return response


class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/communify/home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required()
def home(request):
    user_profile = get_object_or_404(Profile, user=request.user)
    context = {'profile': user_profile, 'user': request.user, 'profile_image': user_profile.image}
    return render(request, 'communifyapp/home.html', context= context )


# @method_decorator(login_required, name="dispatch")
# class ProtectedView(TemplateView):
#     template_name = "secret.html"

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'communifyapp/create_post.html'
    form_class = PostForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            thought = form.save(commit=False)
            thought.user = request.user
            thought.save()
        return render(request, self.template_name, {'form': form})


# class PostTypeView(LoginRequiredMixin, View):
#     template_name = 'communifyapp/posttype.html'
#     form_class = PostTypeForm

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'communifyapp/update_post.html'
    fields = ['text', 'image', 'private', 'type']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("communifyapp/home")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'communifyapp/delete_post.html'

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("communifyapp/home")

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


# ...

class PostView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "communifyapp/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        post = get_object_or_404(Post, pk=pk)
        comments = post.comment_set.all()
        user_profile = get_object_or_404(Profile, user=post.user)

        context['post'] = post
        context['comments'] = comments
        context['profile_image'] = user_profile.image
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.filter(id=self.kwargs['pk']).first()

        if post:
            comments = post.comment_set.all()
        else:
            comments = []

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
        print("this is working")

        if form.is_valid():
            print("workinggggggggggggg")
            name = form.cleaned_data['name']
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                name=name, content=content, post=post
            )
            form = CommentForm()
            context['form'] = form
        else:
            # Print form errors for debugging
            print('Form errors:', form.errors)

        return self.render_to_response(context=context)

class HomeView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "communifyapp/home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        user_profile = get_object_or_404(Profile, user=self.request.user)
        # posts = get_object_or_404(Post, user=self.request.user)
        context['profile'] = user_profile
        context['user'] = self.request.user
        context['profile_image'] = user_profile.image
        # context['posts'] = posts
        return context

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "communifyapp/commentpost.html"

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


@login_required
def profile(request):
    # user = get_object_or_404(CustomUser, username=username)
    user_profile = get_object_or_404(Profile, user= request.user)
    context = {'profile': user_profile, 'user': request.user, 'profile_image': user_profile.image}
    return render(request, 'communifyapp/profile.html', context = context)


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'communifyapp/edit_profile.html'
    fields = ['image', 'about_me']
    success_url = reverse_lazy('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update
        user_profile = get_object_or_404(Profile, user=self.request.user)
        context['profile_image'] = user_profile.image
        return context

    def get_object(self, queryset=None):
        user_profile = get_object_or_404(Profile, user=self.request.user )
        return user_profile
