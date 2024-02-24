from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import NewUser

class SignUpForm(UserCreationForm):
    
    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].label = "Email"
        self.fields["username"].label = "Username"
        self.fields["fname"].label = "Nome"

        
    
    class Meta:
        model = NewUser
        fields = ['username', 'email', 'fname', 'password1', 'password2']