from django import forms
from django.core.exceptions import ValidationError
from .models import Movies,UserMovies
from users.models import CustomUser


class moviesForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        label='Poster Name',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control ", 'placeholder': 'Name'}),
        error_messages={
            'required': 'name is required'
        }
    )
    poster = forms.FileField(
        required=True,
        label='Poster Image',
        initial='',
        widget=forms.FileInput(attrs={'class': "form-control "}),
        error_messages={
            'required': 'file field is required',
            
        }
    )

    class Meta:
        model = Movies
        fields = ['name', 'poster']
    
    def clean_name(self):
        data = self.cleaned_data
        name = data.get('name')
        if name == "" or name is None:
            raise ValidationError(self.fields['name'].error_messages['required'])
        return name

    def clean_poster(self):
        data = self.cleaned_data
        poster = data.get('poster')
        if poster == "" or poster is None:
            raise ValidationError(self.fields['poster'].error_messages['required'])
        return poster


class MoviesAddForm(forms.Form):
    name = forms.CharField(
        required=True,
        label='Poster Name',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control ", 'placeholder': 'Name'}),
        error_messages={
            'required': 'name is required'
        }
    )
    poster = forms.FileField(
        required=True,
        label='Poster Image',
        initial='',
        widget=forms.FileInput(attrs={'class': "form-control "}),
        error_messages={
            'required': 'file field is required',
            
        }
    )



    def clean_name(self):
        data = self.cleaned_data
        name = data.get('name')
        if name == "" or name is None:
            raise ValidationError(self.fields['name'].error_messages['required'])
        return name

    def clean_poster(self):
        data = self.cleaned_data
        poster = data.get('poster')
        if poster == "" or poster is None:
            raise ValidationError(self.fields['poster'].error_messages['required'])
        return poster




class AssignMoviesForm(forms.Form):
    users = forms.ModelMultipleChoiceField(queryset=CustomUser.objects.filter(is_active=True,is_superuser = False), widget=forms.CheckboxSelectMultiple)
    posters = forms.ModelMultipleChoiceField(queryset=Movies.objects.filter(is_active=True), widget=forms.CheckboxSelectMultiple)


    # class Meta:
    #     model = UserMovies
    #     fields = ['user', 'poster']

