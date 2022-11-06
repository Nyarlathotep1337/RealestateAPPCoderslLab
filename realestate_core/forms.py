from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from realestate_core.models import Realtor, Realestate, RealestateType


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control'}),
                               required=False)


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               validators=[validate_password],
                               help_text='Hasło ma być dłuższe niż 8')
    password2 = forms.CharField(label='re-Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        data = super().clean()
        pass1 = data.get('password1')
        if pass1 is not None and pass1 != data.get('password2'):
            raise ValidationError('Hasła nie są identyczne')
        return data


class CreateRealtorForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = '__all__'


class CreateRealestateForm(forms.ModelForm):
    class Meta:
        model = Realestate
        fields = '__all__'


class RealtorForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = '__all__'


class RealestateForm(forms.ModelForm):
    class Meta:
        model = Realestate
        fields = '__all__'


class SellBuyForm(forms.ModelForm):
    class Meta:
        model = RealestateType
        fields = '__all__'
