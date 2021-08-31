from authentication.models import Customer, Seller
from django.contrib.auth.forms import UserCreationForm


class SellerForm(UserCreationForm):
    class Meta:
        model = Seller
        fields = ['email', 'password1', 'password2']
        
class CustomerForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['email', 'password1', 'password2']
