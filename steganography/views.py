from django.shortcuts import render
from .forms import SteganographyForm

def apply_steganography(source_text, hidden_text):
    binary_hidden = ''.join(format(ord(char), '08b') for char in hidden_text)
    result = []
    bin_index = 0

    for char in source_text:
        if char.isalpha() and bin_index < len(binary_hidden):
            if binary_hidden[bin_index] == '1':
                result.append(char.upper())
            else:
                result.append(char.lower())
            bin_index += 1
        else:
            result.append(char)

    return ''.join(result)

def steganography_view(request):
    processed_text = None
    if request.method == 'POST':
        form = SteganographyForm(request.POST)
        if form.is_valid():
            source_text = form.cleaned_data['source_text']
            hidden_text = form.cleaned_data['hidden_text']
            processed_text = apply_steganography(source_text, hidden_text)
    else:
        form = SteganographyForm()

    return render(request, 'steganography_page.html', {'form': form, 'processed_text': processed_text})
