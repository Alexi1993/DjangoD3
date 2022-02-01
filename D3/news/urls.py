from django.urls import path
from .views import news, detail

urlpatterns = [
    path('news_list/', news, name='news'),
    path('new/<str:pk>', detail, name='detail'),
]
