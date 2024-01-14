from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import UserModel, Post
from .forms import UserForm, PostForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin






# Create your views here.

class UserRegistrationView(CreateView):
    model = UserModel
    form_class = UserForm
    # template_name = 'user_registration.html'  #  template link
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration

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