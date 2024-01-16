from django.shortcuts import render, redirect
from django.urls import reverse_lazy 
from django.views import generic
from .models import CustomUser, Post
from .forms import SignupForm, PostForm, LoginForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from django.views import View




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

class PostView(View):
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