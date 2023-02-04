from django.contrib import admin
from clients.models import Clients

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'address', 'phone_number', 'email')
