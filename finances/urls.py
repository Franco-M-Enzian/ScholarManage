from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = "finances"

urlpatterns = [
    path('income/list/', views.IncomeListView.as_view(), name="income_list"),
    # path('expense/list/', views.ExpenseListView.as_view(), name="expense_list"),
    path("income/add/", views.IncomeAddView.as_view(), name="income_add"),
    # path("expense/add/", views.ExpenseAddView.as_view(), name="expense_add"),
    # path("income/delete/", views.IncomeDeleteView.as_view(), name="income_delete"),
    # path("expense/delete/", views.ExpenseDeleteView.as_view(), name="expense_delete"),
]
