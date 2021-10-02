from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"

class AccountView(TemplateView):
    template_name = "account.html"

from. models import Post

### 一覧
### テンプレート名は post_list.html にする必要

from django.views.generic import ListView

class Index(ListView):
    model = Post


### 個別ページ
### テンプレート名は post_detail.html にする必要

from django.views.generic import DetailView

class Detail(DetailView):
    model = Post


### 新規作成
### テンプレート名は post_form.html にする必要

from django.views.generic.edit import CreateView

class Create(CreateView):
    model = Post
    fields = ["title", "body", "category", "tags"]


### 編集

from django.views.generic.edit import UpdateView

class Update(UpdateView):
    model = Post
    fields = ["title", "body", "category", "tags"]


### 削除
### テンプレート名は post_confirm_delete にする必要

from django.views.generic.edit import DeleteView

class Delete(DeleteView):
    model = Post
    # 削除後に移動するURL
    success_url = "/"

### Sign up

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'arataapp/signup.html'
