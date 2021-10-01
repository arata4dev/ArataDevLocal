from django.urls import path

from . import views
from .views import AboutView

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('about/', AboutView.as_view()),
    path('detail/<pk>', views.Detail.as_view(), name="detail"),
]

# pk = primary key (IDのこと)