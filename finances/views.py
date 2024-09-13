from django.urls import reverse_lazy
from django.conf import settings
from .models import Income
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class IncomeListView(LoginRequiredMixin, ListView):
    model = Income
    context_object_name = "incomes"
    template_name = "finances/income_list.html"

    def get_queryset(self):
        return Income.objects.select_related("account").filter(account=self.request.user).all()

class IncomeAddView(LoginRequiredMixin, CreateView):
    model = Income
    fields = ["year", "month", "category", "amount"]
    template_name = "finances/income_add.html"
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    fields = ["year", "month", "category", "amount"]
    template_name = "finances/income_update.html"
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)


class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Income
    template_name = "finances/income_delete.html"
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)
