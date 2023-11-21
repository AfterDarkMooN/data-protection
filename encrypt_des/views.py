from django.shortcuts import render
from Crypto.Cipher import DES
from .forms import EncryptFileForm, DecryptFileForm  # Предполагается, что у вас есть эти формы

def manual_pad(data):
    padding_length = 8 - (len(data) % 8)
    padding = bytes([padding_length] * padding_length)
    return data + padding

def manual_unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]

def encrypt_file_view(request):
    if request.method == 'POST':
        form = EncryptFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            key = form.cleaned_data['key'].encode()
            des = DES.new(key, DES.MODE_ECB)
            data = manual_pad(file.read())
            encrypted_data = des.encrypt(data)
            with open('encrypted_file.des', 'wb') as f:
                f.write(encrypted_data)
            return render(request, 'encrypt_file.html', {'form': form, 'message': 'Файл зашифрован'})
    else:
        form = EncryptFileForm()
    return render(request, 'encrypt_file.html', {'form': form})

def decrypt_file_view(request):
    if request.method == 'POST':
        form = DecryptFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            key = form.cleaned_data['key'].encode()
            des = DES.new(key, DES.MODE_ECB)
            encrypted_data = file.read()
            decrypted_data = des.decrypt(encrypted_data)
            decrypted_data = manual_unpad(decrypted_data)
            with open('decrypted_file', 'wb') as f:
                f.write(decrypted_data)
            return render(request, 'decrypt_file.html', {'form': form, 'message': 'Файл расшифрован'})
    else:
        form = DecryptFileForm()
    return render(request, 'decrypt_file.html', {'form': form})
