from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import UserModel
from .forms import UserForm


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
