from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs ={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label = 'Username or Email'
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs ={'class': 'form-control', 'placeholder': 'passwprd'}))
    
    recaptcha = ReCaptchaField(
        widget = ReCaptchaV2Checkbox()
    )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    recaptcha = ReCaptchaField(
        widget = ReCaptchaV2Checkbox()
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user