from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.game_list, name='game_list'),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
    path('api/games/', views.api_game_list, name='api_game_list'),
    path('api/game/', views.api_game_detail, name='api_game_detail'),
    path('api/game/create/', views.api_game_create, name='api_game_create'),
]
