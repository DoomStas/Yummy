from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', min_length=3, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                                                            'class': 'form-control',
                                                                                                            'id': 'username',
                                                                                                            'data-rule': 'username',
                                                                                                            'data-msg': 'Username'}))
    email = forms.CharField(label='Email', min_length=3, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                                                                      'class': 'form-control',
                                                                                                      'id': 'email',
                                                                                                      'data-rule': 'email',
                                                                                                      'data-msg': 'Email'}))
    password1 = forms.CharField(label='Password',  widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                                     'class': 'form-control',
                                                                                     'id': 'password',
                                                                                     'data-rule': 'password',
                                                                                     'data-msg': 'Password'}))
    password2 = forms.CharField (label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                                             'class': 'form-control',
                                                                                             'id': 'password2',
                                                                                             'data-rule': 'password',
                                                                                             'data-msg': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                               'class': 'form-control',
                                                                               'id': 'username',
                                                                               'data-rule': 'username',
                                                                               'data-msg': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                                   'class': 'form-control',
                                                                                   'id': 'password',
                                                                                   'data-rule': 'password',
                                                                                   'data-msg': 'Password'}))