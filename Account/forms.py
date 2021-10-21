from django import forms
from .models import User

class CustomForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CustomForms, self).__init__(*args, **kwargs)

        if user.is_superuser:
            pass
        else:
            self.fields['vip_date'].disabled = True
            self.fields['first_name'].disabled = True
            self.fields['username'].help_text = 'بر پدر و مادر کسی که این رو خالی بذاره لعنت.'
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'vip_date']


