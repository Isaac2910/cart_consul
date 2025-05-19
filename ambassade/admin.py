from django.contrib import admin
from .models import DemandeCarteConsulaire


@admin.register(DemandeCarteConsulaire)
class DemandeCarteConsulaireAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = (
        "numero_dossier",
        "nom",
        "prenom",
        "date_naissance",
        "nationalite",
        "statut",
        "date_soumission",
    )
    # Champs cliquables menant au détail
    list_display_links = ("numero_dossier", "nom", "prenom")
    # Filtres latéraux
    list_filter = ("statut", "nationalite", "date_soumission")
    # Barre de recherche
    search_fields = ("numero_dossier", "nom", "prenom", "email", "telephone")
    # Ordre par défaut (déjà défini dans Meta, mais on précise pour l’admin)
    ordering = ("-date_soumission",)
    # Champs en lecture seule
    readonly_fields = ("numero_dossier", "date_soumission", "date_mise_a_jour")

    # Organisation des champs dans le formulaire d’édition
    fieldsets = (
        ("Informations personnelles", {
            "fields": (
                ("nom", "prenom"),
                ("date_naissance", "sexe", "nationalite"),
                "adresse",
                ("telephone", "email"),
            )
        }),
        ("Documents à fournir", {
            "fields": (
                "photo_identite",
                "piece_identite",
                "justificatif_domicile",
            )
        }),
        ("Suivi administratif", {
            "fields": (
                "statut",
                "commentaires",
                ("numero_dossier", "date_soumission", "date_mise_a_jour"),
            )
        }),
    )

    # Pour éviter toute modification accidentelle dans la liste
    list_editable = ("statut",)

    # Pagination (25 par page par défaut, ajustable ici)
    list_per_page = 25
