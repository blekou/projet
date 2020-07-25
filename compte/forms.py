from django.forms import ModelForm
from .models import Commande,Client
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 



class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ["user"]

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = '__all__'
        


class MyUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]