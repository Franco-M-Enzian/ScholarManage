from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, birthday, loan_or_benefit, password=None):
        if not username:
            raise "ユーザーネームは必須です。"
        if not email:
            raise "メールアドレスは必須です。"
        if not birthday:
            raise "誕生日は必須です。"
        if not loan_or_benefit:
            raise "奨学金は貸与か給付か選択してください。"

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            birthday=birthday,
            loan_or_benefit=loan_or_benefit,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, birthday, loan_or_benefit, password=None):
        user = self.create_user(
            username,
            email,
            birthday=birthday,
            loan_or_benefit=loan_or_benefit,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    GRADE = [
        ("1", "学部1年"),
        ("2", "学部2年"),
        ("3", "学部3年"),
        ("4", "学部4年"),
    ]
    LOAN_OR_BENEFIT = [
        ("loan", "貸与"),
        ("benefit", "給付"),
    ]
    username = models.CharField("ユーザーネーム", max_length=15, blank=False)
    email = models.EmailField("メールアドレス", unique=True, blank=False)
    birthday = models.DateField("誕生日", blank=False)
    what_grade = models.CharField("学部何年生か", max_length=1, choices=GRADE, blank=True, null=True)
    loan_or_benefit = models.CharField("奨学金は貸与か給付か", max_length=7, choices=LOAN_OR_BENEFIT, blank=False)
    last_login = models.DateTimeField("最後にログインした日時", blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
                    "username", "birthday",
                    "loan_or_benefit"
                ]

    objects = MyUserManager()

    def __str__(self):
        return self.username + " : " + self.email


