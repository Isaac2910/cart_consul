from django.shortcuts import render

def accueil(request):
    return render(request, 'accueil.html')


from django.shortcuts import render, redirect
from .forms import DemandeCarteConsulaireForm

def nouvelle_demande(request):
    if request.method == "POST":
        form = DemandeCarteConsulaireForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("demande_succes")  # Remplacez par votre URL de succès
    else:
        form = DemandeCarteConsulaireForm()
    return render(request, "demande_form.html", {"form": form})


from django.shortcuts import render

def demande_succes(request):
    return render(request, "demande_succes.html")


# views.py
from django.shortcuts import render
from .models import DemandeCarteConsulaire

def liste_demandes(request):
    demandes = DemandeCarteConsulaire.objects.all().order_by("-id")  # plus récentes d’abord
    context = {"demandes": demandes}
    return render(request, "demandes/liste_demandes.html", context)


# views.py
from django.views.generic import DetailView


class DemandeCarteConsulaireDetailView(DetailView):
    model = DemandeCarteConsulaire
    template_name = "demandes/detail_demande.html"   # à créer
    context_object_name = "demande"
