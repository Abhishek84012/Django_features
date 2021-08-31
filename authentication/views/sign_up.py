from authentication.forms.registration import CustomerForm,SellerForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class CustomerSignUpView(CreateView):
    form_class = CustomerForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/sign_up.html'


class SellerSignUpView(CreateView):
    form_class = SellerForm
    success_url = reverse_lazy('login')
    template_name = 'authentication/sign_up.html'
