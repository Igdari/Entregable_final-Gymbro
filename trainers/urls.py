from django.urls import path
from trainers.views import add_trainer , list_trainers, update_trainer , TrainerDeleteView

urlpatterns = [
    path('add-trainer/', add_trainer),
    path('list-trainers/', list_trainers),
    path('update-trainer/<int:pk>/', update_trainer, name='update_trainer'),
    path('delete-trainer/<int:pk>/', TrainerDeleteView.as_view()),
]