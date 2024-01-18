from django.shortcuts import render, redirect
from django.urls import reverse_lazy 
from django.views import generic
from .models import CustomUser, Post
from .forms import SignupForm, PostForm, LoginForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .forms import CommentForm




# Create your views here.

# def signupview(request):
#     if request.method == 'POST':
#         print("form is working", form.data)
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             # username=form.cleaned_data['username']
#             # password=form.cleaned_data['password']
#             # address=form.cleaned_data['address']
#             # gender=form.cleaned_data['password']
#             # contact=form.cleaned_data['contact_no']
            
#             # user = UserModel.objects.create(username=username, password= password, address = address, gender= gender, contact=contact)
            
#             # login(request, user)
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account was created for {username}!')
#             return redirect('login')
#     else:
#         form = SignupForm()
#     return render(request, 'communifyapp/signup.html', {'form': form})
class signUpView(CreateView):
    model = CustomUser
    form_class = SignupForm
    template_name = 'communifyapp/signup.html'
    success_url = reverse_lazy('registration/login') 

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
            # Handle the case when the form is not valid
            
    
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
    

def home(request):
     return render(request, 'communifyapp/home.html')

# @method_decorator(login_required, name="dispatch")
# class ProtectedView(TemplateView):
#     template_name = "secret.html"

class CreatePostView(LoginRequiredMixin,CreateView):
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

class PostView(LoginRequiredMixin,DetailView):
    model = Comment
    template_name = "communifyapp/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        # slug = self.kwargs["slug"]

        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form
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