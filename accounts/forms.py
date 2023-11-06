from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationsForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password','password2')

