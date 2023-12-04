from django import forms
from userr.models import User, Tweets
from django.contrib.auth import authenticate
import re


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("Username is Mandatory")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password:
            raise forms.ValidationError("Password is Mandatory")
        return password

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        authenticated_user = authenticate(username=username, password=password)

        if not authenticated_user:
            raise forms.ValidationError("Not Authenticated User")
        self.user = authenticated_user
        return cleaned_data


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Renter the Password",
        widget=forms.PasswordInput,

    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("Username is Mandatory")
        return username

    def clean_password(self):

        password = self.cleaned_data.get("password")

        if len(password) < 8:
            raise forms.ValidationError("Password must conatin alteast 8 charaters")

        if not re.search(r'[A-Za-z]', password):
            raise forms.ValidationError("Password must contain at least one letter.")

        if not re.search(r'[0-9]', password):
            raise forms.ValidationError("Password must contain at least one digit.")

        if not re.search(r'[!@#$%^&*]', password):
            raise forms.ValidationError("Password must contain at least one special character (!@#$%^&*).")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Passwords Must be same")
        return cleaned_data


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweets
        fields = ['tweet', 'tweet_img']
        widgets = {
            'tweet': forms.TextInput(attrs={'placeholder': 'What\'s happening?'}),
        }
        labels = {
            'tweet': '',
            'tweet_img': '',
        }