from django.db import models
from django.contrib.auth.models import User
import uuid

# --- Modèle DemandeCarteConsulaire ---
class DemandeCarteConsulaire(models.Model):
    STATUT_CHOIX = [
        ('en_attente', 'En attente de traitement'),
        ('en_cours', 'En cours de traitement'),
        ('approuvee', 'Approuvée'),
        ('rejetee', 'Rejetée'),
    ]

    numero_dossier = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Numéro de dossier"
    )
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=20)
    nationalite = models.CharField(max_length=50)
    adresse = models.TextField()
    telephone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


    photo_identite = models.ImageField(upload_to='documents/photos_identite/')
    piece_identite = models.FileField(upload_to='documents/pieces_identite/')
    justificatif_domicile = models.FileField(upload_to='documents/justificatifs_domicile/')

    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOIX,
        default='en_attente'
    )
    commentaires = models.TextField(
        blank=True,
        null=True,
        help_text="Commentaires internes de l’administration"
    )

    date_soumission = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_soumission']
        verbose_name = "Demande de carte consulaire"
        verbose_name_plural = "Demandes de cartes consulaires"

    def __str__(self):
        return f"{self.nom.upper()} {self.prenom.capitalize()} - {self.numero_dossier}"


# --- Modèle AgentConsulaire ---
class AgentConsulaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom_complet = models.CharField(max_length=150)
    fonction = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    actif = models.BooleanField(default=True)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Agent consulaire"
        verbose_name_plural = "Agents consulaires"

    def __str__(self):
        return f"{self.nom_complet} ({self.fonction})"
