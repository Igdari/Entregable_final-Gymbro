from django.contrib import admin
from users.models import UserProfile, WelcomePage

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('phone', 'birth_date')

@admin.register(WelcomePage)
class WelcomePageAdmin(admin.ModelAdmin):
    list_display = ('welcome_greetings', 'welcome_picture')