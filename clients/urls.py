from django.urls import path
from clients.views import add_client , list_clients, client, update_client, ClientDeleteView

urlpatterns = [
    path('add-client/', add_client),
    path('list-clients/', list_clients),
    path('client/', client),
    path('update-client/<int:pk>/', update_client, name='update_client'),
    path('delete-client/<int:pk>/', ClientDeleteView.as_view()),
]