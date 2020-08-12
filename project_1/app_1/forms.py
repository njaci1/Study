from django import forms
from django.core import validators

def check_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('NAME MUST START WITH Z')

class BasicForm(forms.Form):
    name = forms.CharField(validators=[check_z])
    email = forms.EmailField()
    verifyEmail = forms.EmailField(label='enter email again')
    text = forms.CharField(widget=forms.Textarea)
    botchecker = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        clean_data = super().clean()
        email = clean_data['email']
        vemail = clean_data['verifyEmail']

        if email != vemail:
            raise forms.ValidationError("Emails not matching")
