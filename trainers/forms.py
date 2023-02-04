from django import forms

CONDITION_CHOICES = (
        ('Funcional', 'Funcional'),
        ('Spinning', 'Spinning'),
        ('Crossfit', 'Crossfit'),
        ('Arte-Marcial', 'Arte-Marcial'),
    )

class TrainerForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, label='Nombre')
    last_name = forms.CharField(max_length=50, required=True, label='Apellido')
    phone_number = forms.CharField(max_length=20, required=False, label='N° de Telefono')
    email = forms.EmailField(required=False, label='Correo Electrónico')
    teaches = forms.ChoiceField(required=True, choices = CONDITION_CHOICES, label='Enseña')
    is_free = forms.BooleanField(required=False, label='Esta diponible')