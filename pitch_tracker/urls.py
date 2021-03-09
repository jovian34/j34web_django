from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(f'game/<int:game_id>/', views.game, name='game'),
]
