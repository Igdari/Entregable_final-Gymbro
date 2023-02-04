from django import forms

CONDITION_CHOICES = (
        ('2 vez por semana', '2 vez por semana'),
        ('3 veces por semana', '3 veces por semana'),
        ('5 vez por semana', '5 veces por semana'),
        ('Libre', 'Libre'),
    )


class PlanForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre del Plan')
    detail = forms.ChoiceField(required=True, choices = CONDITION_CHOICES, label='Detalle')
    cost = forms.FloatField()