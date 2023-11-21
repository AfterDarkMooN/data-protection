from django.urls import path
from .views import encrypt_file_view, decrypt_file_view

urlpatterns = [
    path('encrypt-file/', encrypt_file_view, name='encrypt_file'),
    path('decrypt-file/', decrypt_file_view, name='decrypt_file'),
]
