
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import ExtractMonth
from .models import Expense
from .forms import ExpenseForm

# Function to add expense
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    
    return render(request, 'expenses/add_expense.html', {'form': form })

# Function to view & filter expenses
def expense_list(request):
    months = list(range(1, 13))
    category = request.GET.get('category')
    month = request.GET.get('month')
    expenses = Expense.objects.all()
    if category and category != "All":
        expenses = expenses.filter(category=category)
    if month:
        expenses = expenses.annotate(month=ExtractMonth('date')).filter(month=int(month))
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'months': months})

# Function to edit expense
def edit_expense(request, id):
    #expense = Expense.objects.get(id=id)
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'expenses/edit_expense.html', {'form': form})

# Function to delete expense
def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    expense.delete()
    return redirect('expense_list')
