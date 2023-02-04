from django.urls import path
from trainers.views import add_trainer , list_trainers

urlpatterns = [
    path('add-trainer/', add_trainer),
    path('list-trainers/', list_trainers),
]