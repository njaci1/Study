from django import forms
from app_3 import UserProfileInfo

class UserProfileInfoForm(forms.ModelForm):
    portfolio = forms.URLField(required=False)
    picture = forms.ImageField(required=False)


    #Meta class connects the above class with the class in the model.py file
    class Meta():
        model = UserProfileInfo
        exclude = ('user',)
