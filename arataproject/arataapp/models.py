from django.db import models

# Create your models here.

from django.urls import reverse_lazy


class Category(models.Model):
    name = models.CharField(
        max_length = 255,
        blank = False,
        null = False,
        unique = True,
    )

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(
        max_length = 255,
        blank = False,
        null = False,
        unique = True,
    )

    def __str__(self):
        return self.name

class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add = True,
        editable = False,
        blank = False,
        null = False,
    )

    updated = models.DateTimeField(
        auto_now = True,
        editable = False,
        blank = False,
        null = False,
    )

    title = models.CharField(
        max_length = 255,
        blank = False,
        null = False,
    )

    body = models.TextField(
        blank = True,
        null = False,
    )

    category = models.ForeignKey(
        Category, 
        on_delete = models.CASCADE
        )
    
    tags = models.ManyToManyField(
        Tag,
        blank = True,
    )

    def __str__(self):
        return self.title

    # 新規投稿作成後に作成したポストが表示される、そのためのリンクを教えてあげる関数
    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])

###

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)

# unique = True にすると空欄も不可になる
# Userモデルをプロジェクト全体で使うために Settings.py に以下追加
# AUTH_USER_MODEL = 'arataapp.User'