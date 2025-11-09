from django.urls import path
from . import views

app_name = "game"
urlpatterns = [
    path("", views.index, name="index"),                    # Accueil + start game
    path("scenario/", views.scenario, name="scenario"),     # Génération scénario + affichage scénario
    path("result/", views.result, name="result"),           # Évaluation scénario + résultat
]
