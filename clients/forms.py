from django import forms
from clients.models import Clients

class ClientForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, label='Nombre')
    last_name = forms.CharField(max_length=50, required=True, label='Apellido')
    birth_date = forms.DateField(required=True, label='Fecha de Nacimiento')
    address = forms.CharField(max_length=300, required=False, label='Dirección')
    phone_number = forms.CharField(max_length=20, required=False, label='N° de Telefono')
    email = forms.EmailField(required=False, label='Correo Electrónico')