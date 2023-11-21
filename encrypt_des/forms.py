from django import forms
from django.core.exceptions import ValidationError

class EncryptFileForm(forms.Form):
    file = forms.FileField()
    key = forms.CharField(max_length=8, min_length=8)

    def clean_key(self):
        key = self.cleaned_data['key']
        if len(key) != 8:
            raise ValidationError("Длина ключа должна быть ровно 8 символов.")
        return key

class DecryptFileForm(forms.Form):
    file = forms.FileField()
    key = forms.CharField(max_length=8, min_length=8)

    def clean_key(self):
        key = self.cleaned_data['key']
        if len(key) != 8:
            raise ValidationError("Длина ключа должна быть ровно 8 символов.")
        return key
