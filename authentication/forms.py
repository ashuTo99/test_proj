from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=False,
        label='Your Email',
        widget=forms.TextInput(
            attrs={'class': "form-control",
                   'placeholder': 'Email'}),
        error_messages={
            'required': 'Email is required'
        }
    )
    password = forms.CharField(
        required=False,
        label='Your Password',
        widget=forms.PasswordInput(
            attrs={'class': "form-control",
                   'placeholder': 'Password'}),
        error_messages={
            'required': 'Password is required'
        }
    )

    def clean_email(self):
        data = self.cleaned_data
        email = data.get('email')
        if email == "" or email is None:
            raise ValidationError(self.fields['email'].error_messages['required'])
        return email

    def clean_password(self):
        data = self.cleaned_data
        password = data.get('password')
        if password == "" or password is None:
            raise ValidationError(self.fields['password'].error_messages['required'])
        return password


# class passwordChangeForm(forms.ModelForm):
#     old_password = forms.CharField(
#         required=False,
#         label='Old Password',
#         widget=forms.PasswordInput(
#             attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': "Old password"}),
#         error_messages={
#             'required': 'Old password is required !',
#             'error_messages': 'Old password is not correct.',
#         }
#     )
#     new_password = forms.CharField(
#         required=False,
#         label='New Password',
#         widget=forms.PasswordInput(
#             attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': "New password"}),
#         error_messages={
#             'required': 'New password is required.',
#             'min_value': 'New password should be at least 8 charcter.'
#         }
#     )
#     confirm_password = forms.CharField(
#         required=False,
#         label='Confirm Password',
#         widget=forms.PasswordInput(
#             attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': "Confirm password"}),
#         error_messages={
#             'required': 'Confirm password field is required.',
#             'error_messages': 'Confirm password and new password must match.',
#             'min_value': 'Confirm password should be at least 8 charcter.',
#         }
#     )

#     class Meta:
#         model = Employee
#         fields = ['old_password', 'new_password', 'confirm_password']

#     def clean_old_password(self):
#         data = self.cleaned_data
#         password = self.instance.password
#         old_password = data.get('old_password')
#         if old_password == "" or old_password is None:
#             raise ValidationError(self.fields['old_password'].error_messages['required'])
#         elif old_password is not None or not old_password:
#             isChecked = check_password(old_password, password)
#             if not isChecked:
#                 raise ValidationError(self.fields['old_password'].error_messages['error_messages'])
#         return old_password

#     def clean_new_password(self):
#         data = self.cleaned_data
#         new_password = data.get('new_password')
#         if new_password == "" or new_password is None:
#             raise ValidationError(self.fields['new_password'].error_messages['required'])
#         elif 8 > len(new_password) > 0:
#             raise ValidationError(self.fields['new_password'].error_messages['min_value'])
#         return new_password

#     def clean_confirm_password(self):
#         data = self.cleaned_data
#         new_password = data.get('new_password')
#         confirm_password = data.get('confirm_password')
#         if confirm_password == "" or confirm_password is None:
#             raise ValidationError(self.fields['confirm_password'].error_messages['required'])
#         elif 8 > len(confirm_password) > 0:
#             raise ValidationError(self.fields['confirm_password'].error_messages['min_value'])
#         elif new_password != confirm_password:
#             raise ValidationError(self.fields['confirm_password'].error_messages['error_messages'])
#         return confirm_password

