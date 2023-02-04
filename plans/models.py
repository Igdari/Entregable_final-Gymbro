from django.db import models

CONDITION_CHOICES = (
        ('2 vez por semana', '2 vez por semana'),
        ('3 veces por semana', '3 veces por semana'),
        ('5 vez por semana', '5 veces por semana'),
        ('Libre', 'Libre'),
    )

class Plans(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    cost = models.FloatField()
    
    def __str__(self):
        return self.name