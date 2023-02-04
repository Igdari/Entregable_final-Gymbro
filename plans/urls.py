from django.urls import path
from plans.views import add_plan , list_plans

urlpatterns = [
    path('add-plan/', add_plan),
    path('list-plans/', list_plans),
]