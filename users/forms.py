from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser


class userForm(forms.ModelForm):
    name = forms.CharField(
        required=False,
        label='Name',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Name'}),
        error_messages={
            'required': 'name is required.'
        }
    )
    email = forms.EmailField(
        required=False,
        label='Email',
        initial='',
        widget=forms.TextInput(attrs={'class': "form-control form-control-solid form-control-lg"}),
        error_messages={
            'required': 'email is required',
            'invalid': 'email not valid'
        }
    )

    class Meta:
        model = CustomUser
        fields = ['name', 'email']

    def clean_name(self):
        data = self.cleaned_data
        name = data.get('name')
        if name == "" or name is None:
            raise ValidationError(self.fields['name'].error_messages['required'])
        return name

    def clean_email(self):
        data = self.cleaned_data
        email = data.get('email')
        if email == "" or email is None:
            raise ValidationError(self.fields['email'].error_messages['required'])
        return email


class UserAddForm(forms.Form):
    name = forms.CharField(
        required=False,
        label='Name',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control ", 'placeholder': 'Name'}),
        error_messages={
            'required': 'name is required'
        }
    )
    email = forms.EmailField(
        required=False,
        label='Email',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control ", 'placeholder': 'Email'}),
        error_messages={
            'required': 'email field is required',
            'invalid': 'email is invalid',
            'exists': 'email already exists'
        }
    )

    password = forms.CharField(
        required=False,
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class': "form-control ", 'placeholder': 'Password'}),
        error_messages={
            'required': 'password field is required',
        }
    )
    confirm_password = forms.CharField(
        required=False,
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={'class': "form-control ", 'placeholder': 'Confirm password'}),
        error_messages={
            'required': 'confirm password field is required',
            'validators': 'password and confirm password must match'
        }
    )

    def clean_name(self):
        data = self.cleaned_data
        name = data.get('name')
        if name == "" or name is None:
            raise ValidationError(self.fields['name'].error_messages['required'])
        return name

    def clean_email(self):
        data = self.cleaned_data
        email = data.get('email')
        user_email = CustomUser.objects.filter(email=email).exists()
        if email == "" or email is None:
            raise ValidationError(self.fields['email'].error_messages['required'])
        elif user_email:
            raise ValidationError(self.fields['email'].error_messages['exists'])
        return email


    def clean_password(self):
        data = self.cleaned_data
        password = data.get('password')
        if password == "" or password is None:
            raise ValidationError(self.fields['password'].error_messages['required'])
        return password

    def clean_confirm_password(self):
        data = self.cleaned_data
        confirm_password = data.get('confirm_password')
        if confirm_password == "" or confirm_password is None:
            raise ValidationError(self.fields['confirm_password'].error_messages['required'])
        elif confirm_password != data.get('password'):
            raise ValidationError(self.fields['confirm_password'].error_messages['validators'])
        return confirm_password


