from django import forms

class EncryptionForm(forms.Form):
    input_text = forms.CharField(label='Текст для шифрования', widget=forms.Textarea)
    key = forms.IntegerField(label='Ключ')

class DecryptionForm(forms.Form):
    file_name = forms.CharField(label='Имя файла')
    key = forms.IntegerField(label='Ключ')