from django.contrib import admin
from trainers.models import Trainers

@admin.register(Trainers)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'teaches')
    list_filter = ('teaches',)
    search_fields = ('name',)