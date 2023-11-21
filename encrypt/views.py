import os
from django.shortcuts import render
from .forms import EncryptionForm, DecryptionForm

def encrypt_char(char, key, alphabet_size=1114111):  # Максимальное значение Unicode
    return chr((ord(char) + key) % alphabet_size)

def decrypt_char(char, key, alphabet_size=1114111):
    return chr((ord(char) - key + alphabet_size) % alphabet_size)

def encrypt(text, key):
    return ''.join(encrypt_char(char, key) for char in text)

def decrypt(text, key):
    return ''.join(decrypt_char(char, key) for char in text)

def encryption_view(request):
    if request.method == 'POST':
        form = EncryptionForm(request.POST)
        if form.is_valid():
            if os.path.exists('encrypted.txt'):
                os.remove('encrypted.txt')
            encrypted_text = encrypt(form.cleaned_data['input_text'], form.cleaned_data['key'])
            # Запись в файл
            with open('encrypted.txt', 'w') as file:
                file.write(encrypted_text)
            return render(request, 'encryption_page.html', {'form': form, 'message': 'Текст зашифрован и записан в файл'})
    else:
        form = EncryptionForm()
    return render(request, 'encryption_page.html', {'form': form})

def decryption_view(request):
    if request.method == 'POST':
        form = DecryptionForm(request.POST)
        if form.is_valid():
            file_name = form.cleaned_data['file_name']
            key = form.cleaned_data['key']
            if os.path.exists(file_name):
                with open(file_name, 'r') as file:
                    encrypted_text = file.read()
                decrypted_text = decrypt(encrypted_text, key)
                return render(request, 'decryption_page.html', {'form': form, 'decrypted_text': decrypted_text})
            else:
                return render(request, 'decryption_page.html', {'form': form, 'error': 'Файл не найден'})
    else:
        form = DecryptionForm()
    return render(request, 'decryption_page.html', {'form': form})