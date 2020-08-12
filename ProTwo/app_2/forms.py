from django import forms
from app_2.models import USERS


class NewUserForm(forms.ModelForm):
    class Meta():
        model = USERS
        fields = '__all__'
