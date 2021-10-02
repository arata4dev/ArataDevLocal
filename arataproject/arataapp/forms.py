# 後から作ったファイル、ファイル名変更可能だが普通は forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        # commit=Falseだと、DBに保存されない。
        # メールアドレスが他人と被っているとユーザー名とかだけ保存されてしまうため
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.save()
        return user

    # このままではメールアドレスの認証が出来ないので本番URLを設定したあとにRevisit
    # https://youtu.be/yl-OXaAiwGU
