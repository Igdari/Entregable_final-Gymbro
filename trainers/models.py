from django.db import models

CONDITION_CHOICES = (
        ('Funcional', 'Funcional'),
        ('Spinning', 'Spinning'),
        ('Crossfit', 'Crossfit'),
        ('Arte-Marcial', 'Arte-Marcial'),
    )

class Trainers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    teaches = models.CharField(max_length=50, choices = CONDITION_CHOICES)

    def __str__(self):
        return self.name