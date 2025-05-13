from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = "finances"

urlpatterns = [
    path("income/list/", views.IncomeListView.as_view(), name="income_list"),
    path("expense/list/", views.ExpenseListView.as_view(), name="expense_list"),
    path("income/add/", views.IncomeAddView.as_view(), name="income_add"),
    path("expense/add/", views.ExpenseAddView.as_view(), name="expense_add"),
    path(
        "income/<int:pk>/update/",
        views.IncomeUpdateView.as_view(),
        name="income_update",
    ),
    path(
        "expense/<int:pk>/update/",
        views.ExpenseUpdateView.as_view(),
        name="expense_update",
    ),
    path(
        "income/<int:pk>/delete/",
        views.IncomeDeleteView.as_view(),
        name="income_delete",
    ),
    path(
        "expense/<int:pk>/delete/",
        views.ExpenseDeleteView.as_view(),
        name="expense_delete",
    ),
]
