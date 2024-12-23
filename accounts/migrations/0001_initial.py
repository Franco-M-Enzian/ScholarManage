# Generated by Django 4.2 on 2024-09-12 23:54

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=15, verbose_name='ユーザーネーム')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='メールアドレス')),
                ('birthday', models.DateField(verbose_name='誕生日')),
                ('what_grade', models.CharField(blank=True, choices=[('学部1年', '学部1年'), ('学部2年', '学部2年'), ('学部3年', '学部3年'), ('学部4年', '学部4年')], max_length=4, null=True, verbose_name='学部何年生ですか？')),
                ('live_with_family', models.CharField(choices=[('はい', 'はい'), ('いいえ', 'いいえ')], max_length=3, verbose_name='家族と同居していますか？')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='最後にログインした日時')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', accounts.models.MyUserManager()),
            ],
        ),
    ]
