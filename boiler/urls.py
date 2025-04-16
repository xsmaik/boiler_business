from django.urls import path
from . import views
from .views import chat_ids_api


# urlpatterns = [
#     path('', views.index, name='index'),  # Главная страница
# ]
urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('api/chat-ids/', chat_ids_api, name='chat_ids_api'),
]
