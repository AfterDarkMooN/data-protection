from django import forms

class SteganographyForm(forms.Form):
    source_text = forms.CharField(widget=forms.Textarea, label='Исходный текст')
    hidden_text = forms.CharField(widget=forms.Textarea, label='Текст для скрытия')