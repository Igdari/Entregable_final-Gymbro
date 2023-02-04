from django.db import models

class Clients(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)    
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    
    
    def __str__(self):
        return f'{self.first_name}, {self.last_name} - {self.birth_date} - {self.address} - {self.phone_number} - {self.email}' 