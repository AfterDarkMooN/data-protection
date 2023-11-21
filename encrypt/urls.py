from django.conf.urls import url
from .views import encryption_view, decryption_view

urlpatterns = [
    url(r'^encrypt/$', encryption_view, name='encrypt'),
    url(r'^decrypt/$', decryption_view, name='decrypt'),
]