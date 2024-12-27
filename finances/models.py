from django.db import models
from accounts.models import Account


class AbstractIncome(models.Model):
    MONTH = [
        ('1月', '1月'),
        ('2月', '2月'),
        ('3月', '3月'),
        ('4月', '4月'),
        ('5月', '5月'),
        ('6月', '6月'),
        ('7月', '7月'),
        ('8月', '8月'),
        ('9月', '9月'),
        ('10月', '10月'),
        ('11月', '11月'),
        ('12月', '12月'),
    ]
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    year = models.CharField("年を入力", max_length=4, blank=False)
    month = models.CharField("月を選択", max_length=10, choices=MONTH, blank=False)
    amount = models.CharField("金額を入力", max_length=7, blank=False)

    class Meta:
        abstract = True


class Income(AbstractIncome):
    CATEGORY = [
        ("家庭からの給付", "家庭からの給付"),
        ("日本学生支援機構の奨学金", "日本学生支援機構の奨学金"),
        ("日本学生支援機構以外の奨学金", "日本学生支援機構以外の奨学金"),
        ("アルバイト等収入", "アルバイト等収入"),
        ("その他", "その他"),
    ]
    category = models.CharField("カテゴリーを選択", max_length=14, choices=CATEGORY, blank=False)

    def __str__(self):
        return f"{self.account.username} {self.year}年{self.month} {self.category} {self.amount}円"


class Expense(AbstractIncome):
    CATEGORY = [
        ("学費", "学費"),
        ("修学費", "修学費"),
        ("食費", "食費"),
        ("光熱水料通信費", "光熱水料通信費"),
        ("その他", "その他"),
    ]
    category = models.CharField("カテゴリーを選択", max_length=7, choices=CATEGORY, blank=False)

    def __str__(self):
        return f"{self.account.username} {self.year}年{self.month} {self.category} {self.amount}円"
