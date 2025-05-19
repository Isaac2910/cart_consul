from django import forms
from .models import DemandeCarteConsulaire


class DemandeCarteConsulaireForm(forms.ModelForm):
    """Formulaire stylé pour la demande de carte consulaire.
    Les attributs HTML correspondent aux classes/placeholder utilisés
    dans le fichier static/style.css et le template fourni."""

    # Options du champ Sexe
    SEXE_CHOICES = [
        ("", "--- Sélectionnez ---"),
        ("M", "Masculin"),
        ("F", "Féminin"),
        ("A", "Autre / Préfère ne pas dire"),
    ]

    # Champ ré‑écrit pour injecter le widget + classes
    sexe = forms.ChoiceField(
        choices=SEXE_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Sexe",
    )

    class Meta:
        model = DemandeCarteConsulaire
        fields = [
            "nom",
            "prenom",
            "date_naissance",
            "sexe",
            "nationalite",
            "adresse",
            "telephone",
            "email",
            "photo_identite",
            "piece_identite",
            "justificatif_domicile",
        ]
        widgets = {
            "nom": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": " ",
            }),
            "prenom": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": " ",
            }),
            "date_naissance": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": " ",
            }),
            "nationalite": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": " ",
            }),
            "adresse": forms.Textarea(attrs={
                "rows": 3,
                "class": "form-control",
                "placeholder": " ",
            }),
            "telephone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": " ",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": " ",
            }),
            "photo_identite": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
            "piece_identite": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
            "justificatif_domicile": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
        }
        labels = {
            "nom": "Nom",
            "prenom": "Prénom",
            "date_naissance": "Date de naissance",
            "sexe": "Sexe",
            "nationalite": "Nationalité",
            "adresse": "Adresse",
            "telephone": "Téléphone",
            "email": "E-mail",
            "photo_identite": "Photo d’identité",
            "piece_identite": "Pièce d’identité",
            "justificatif_domicile": "Justificatif de domicile",
        }

    # Validation personnalisée : téléphone ≥ 8 chiffres
    def clean_telephone(self):
        tel = self.cleaned_data["telephone"]
        digits = [c for c in tel if c.isdigit()]
        if len(digits) < 8:
            raise forms.ValidationError("Le numéro de téléphone doit contenir au moins 8 chiffres.")
        return tel
