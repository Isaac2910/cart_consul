from django.urls import path
from . import views


app_name = "cartes_consulaires"

urlpatterns = [
    path("demande/nouvelle/", views.nouvelle_demande, name="demande_nouvelle"),
    path("demande/succes/", views.demande_succes, name="demande_succes"),
    path("demandes/", views.liste_demandes, name="liste_demandes"),

    
    path("demandes/<int:pk>/", views.DemandeCarteConsulaire, name="detail_demande"),
]
