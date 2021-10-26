from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class CustomForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CustomForms, self).__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['phone'].required = True
        self.fields['vip_date'].required = False
        self.fields['username'].help_text = 'بر پدر و مادر کسی که این رو خالی بذاره لعنت.'
        if user.is_superuser:
            pass
        else:
            self.fields['vip_date'].disabled = True
            self.fields['email'].disabled = True
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','phone', 'vip_date']
        labels = {
            'username': 'نام کاربری',
            'first_name': 'نام',
            'vip_date': 'پایان اشتراک شما:',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
        }




class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    phone = forms.IntegerField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone')

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.extra_field = self.cleaned_data["phone"]
        if commit:
            user.save()
        return user