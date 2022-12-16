from django.views import generic
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm

User = get_user_model()


class RegisterUserView(generic.CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "auth_user/register.html"



