from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User 
from users.models import Seller


class UserRegisterForm(UserCreationForm):

    groups = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'groups']


class CustomUserChangeForm(UserChangeForm):
    
    groups = forms.ModelChoiceField(queryset=Group.objects.all(), blank=True)
    
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'username', 'placeholder':'Your username..'})
        self.fields['first_name'].widget.attrs.update({'class':'first_name', 'placeholder':'Your first_name..'})
        self.fields['last_name'].widget.attrs.update({'class':'last_name', 'placeholder':'Your last_name..'})
        self.fields['email'].widget.attrs.update({'class':'email', 'placeholder':'Your email..'})
        self.fields['groups'].widget.attrs.update({'class':'groups'})
        del self.fields['password']

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'groups']
        


class SellerChangeForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(SellerChangeForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs.update({'class':'gender'})
        self.fields['phone_number'].widget.attrs.update({'class':'phone_number', 'placeholder':'Your phone_number..'})
        self.fields['age'].widget.attrs.update({'class':'age'})

    class Meta:
        model = Seller
        fields = ['gender','phone_number', 'age']    



class UserLoginForm(forms.Form):
    username = forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']