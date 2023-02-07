from django.urls import path
from plans.views import add_plan, list_plans, update_plan, delete_plan

urlpatterns = [
    path('add-plan/', add_plan),
    path('list-plans/', list_plans),
    path('update-plan/<int:pk>/', update_plan, name='update_plan'),
    path('delete-plan/<int:pk>/', delete_plan, name='delete_plan' ),
]