from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"


###

from django.views.generic import ListView, DetailView
from. models import Post

# 簡単に一覧を作るためのView
# ListViewは自動的に post_list.html というファイルを探してくれる
class Index(ListView):
    model = Post

# 簡単に詳細ページを作るためのView
class Detail(DetailView):
    model = Post