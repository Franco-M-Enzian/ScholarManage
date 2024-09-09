from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, birthday, live_alone_or_with_family, password=None):
        if not username:
            raise "ユーザーネームは必須です。"
        if not email:
            raise "メールアドレスは必須です。"
        if not birthday:
            raise "誕生日は必須です。"
        if not live_alone_or_with_family:
            raise "YesもしくはNoと入力してください。"

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            birthday=birthday,
            live_alone_or_with_family=live_alone_or_with_family,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, birthday, live_alone_or_with_family, password=None):
        user = self.create_user(
            username,
            email,
            birthday=birthday,
            live_alone_or_with_family=live_alone_or_with_family,
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
    YES_OR_NO = [
        ("Yes", "はい"),
        ("No", "いいえ"),
    ]
    username = models.CharField("ユーザーネーム", max_length=15, blank=False)
    email = models.EmailField("メールアドレス", unique=True, blank=False)
    birthday = models.DateField("誕生日", blank=False)
    what_grade = models.CharField("学部何年生ですか？", max_length=1, choices=GRADE, blank=True, null=True)
    live_alone_or_with_family = models.CharField("家族と同居していますか？", max_length=7, choices=YES_OR_NO, blank=False)
    last_login = models.DateTimeField("最後にログインした日時", blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
                    "username", "birthday",
                    "live_alone_or_with_family"
                ]

    objects = MyUserManager()

    def __str__(self):
        return self.username + " : " + self.email
