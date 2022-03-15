from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.DisplayMemo, name = 'display_memo'),
    path('memo/', views.MemoView, name='memo_view')
]