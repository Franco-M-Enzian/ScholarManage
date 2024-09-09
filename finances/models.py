from django.db import models
from accounts.models import Account


class Income(models.Model):
    MONTH = [
        ('january', '1月'),
        ('february', '2月'),
        ('march', '3月'),
        ('april', '4月'),
        ('may', '5月'),
        ('june', '6月'),
        ('july', '7月'),
        ('august', '8月'),
        ('september', '9月'),
        ('october', '10月'),
        ('november', '11月'),
        ('december', '12月'),
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    year = models.CharField("年を入力", max_length=4, blank=False)
    month = models.CharField("月を選択", max_length=10, choices=MONTH, blank=False)
    amount = models.CharField("金額を入力：円", max_length=7, blank=False)

    class Meta:
        abstract = True


class TotalIncome(Income):
    CATEGORY = [
        ("From family", "家庭からの給付"),
        ("Scholarship", "日本学生支援機構の奨学金"),
        ("Other scholarship", "日本学生支援機構以外の奨学金"),
        ("Income from PT job etc.", "アルバイト等収入"),
        ("Other", "その他"),
    ]
    category = models.CharField("カテゴリーを選択", max_length=25, choices=CATEGORY, blank=False)


class ExpenseIfNotAlone(Income):
    CATEGORY = [
        ("Tuition", "学費"),
        ("Tuition(Textbook fee etc.)", "修学費"),
        ("Food expenses", "食費"),
        ("Communication costs", "通信費"),
        ("Other", "その他"),
    ]
    category = models.CharField("カテゴリーを選択", max_length=26, choices=CATEGORY, blank=False)


class ExpenseIfAlone(Income):
    CATEGORY = [
        ("Tuition", "学費"),
        ("Tuition(Textbook fee etc.)", "修学費"),
        ("Food expenses", "食費"),
        ("Utility and communication costs", "光熱水料通信費"),
        ("Other", "その他"),
    ]
    category = models.CharField("カテゴリーを選択", max_length=35, choices=CATEGORY, blank=False)
