from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

account_view = views.AccountView.as_view()

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('detail/<pk>', views.Detail.as_view(), name="detail"),
    path('create/', views.Create.as_view(), name="create"),
    path('update/<pk>', views.Update.as_view(), name="update"),
    path('delte/<pk>', views.Delete.as_view(), name="delete"),
    
    path('about/', views.AboutView.as_view()),
    path('account/', login_required(account_view), name="account"),
]

# pk = primary key (IDのこと)