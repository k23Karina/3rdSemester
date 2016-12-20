from django import  forms
from django.contrib.auth import authenticate,login,logout,get_user_model
from .models import Deal
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label="", help_text="", widget=forms.TextInput(
        attrs={'class': 'search-input login-input', 'placeholder': 'Username'}))
    password = forms.CharField(label="", help_text="", widget=forms.PasswordInput(
        attrs={'class': 'search-input login-input', 'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Invalid username or password')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="", help_text="", widget=forms.TextInput(
        attrs={'class': 'search-input login-input', 'placeholder': 'Username'}))
    password = forms.CharField(label="", help_text="", widget=forms.PasswordInput(
        attrs={'class': 'search-input login-input', 'placeholder': 'Password'}))
    email = forms.CharField(label="", help_text="", widget=forms.TextInput(
        attrs={'class': 'search-input login-input', 'placeholder': 'Email'}))
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
        ]
    def clean(self, *args, **kwargs):
        email=self.cleaned_data.get('email')
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return super(UserRegistrationForm, self).clean(*args, **kwargs)


class DealForm(forms.ModelForm):
    telephone = forms.CharField(label="", help_text="", widget=forms.TextInput(
        attrs={'class': 'search-input login-input', 'placeholder': 'Telephone'}))
    adress = forms.CharField(label="", help_text="", widget=forms.TextInput(
        attrs={'class': 'search-input login-input', 'placeholder': 'Adress'}))
    class Meta:
        model = Deal
        fields = [
            'adress',
            'telephone',
        ]
    def clean(self, *args, **kwargs):
        return super(DealForm, self).clean(*args, **kwargs)
