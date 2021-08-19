from django.urls import reverse_lazy
from django.views.generic import CreateView
from authentication.admin import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/sign_up.html'
