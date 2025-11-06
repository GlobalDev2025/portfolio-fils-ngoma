from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('projets/', views.projets, name='projets'),
    path('projets/<int:pk>/', views.detail_projet, name='detail_projet'),
    path('telecharger-cv/', views.telecharger_cv, name='telecharger_cv'),
]