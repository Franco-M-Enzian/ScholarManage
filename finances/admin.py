from django.contrib import admin
from .models import TotalIncome, ExpenseIfNotAlone, ExpenseIfAlone

admin.site.register(TotalIncome)
admin.site.register(ExpenseIfNotAlone)
admin.site.register(ExpenseIfAlone)
