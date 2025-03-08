from django.urls import path
from .views import add_expense, expense_list, edit_expense, delete_expense

urlpatterns = [
    path('add/', add_expense, name='add_expense'),
    path('', expense_list, name='expense_list'),
    path('edit/<int:id>/', edit_expense, name='edit_expense'),
    path('delete/<int:pk>/', delete_expense, name='delete_expense'),
]
