from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404
from django.contrib import messages
import os
from django.conf import settings
from .models import Competence, Projet, MessageContact, CV
from .forms import FormulaireContact

def accueil(request):
    competences = Competence.objects.all()
    projets = Projet.objects.all()[:6]
    cv_actif = CV.objects.filter(est_actif=True).first()
    
    if request.method == 'POST':
        formulaire = FormulaireContact(request.POST)
        if formulaire.is_valid():
            message = formulaire.save(commit=False)
            message.email_verifie = True
            message.save()
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('accueil')
    else:
        formulaire = FormulaireContact()
    
    context = {
        'competences': competences,
        'projets': projets,
        'formulaire': formulaire,
        'cv_actif': cv_actif,
    }
    return render(request, 'accueil.html', context)

def projets(request):
    tous_les_projets = Projet.objects.all()
    categories = Projet.CATEGORIE_CHOICES
    cv_actif = CV.objects.filter(est_actif=True).first()
    
    categorie_filtre = request.GET.get('categorie', '')
    if categorie_filtre:
        tous_les_projets = tous_les_projets.filter(categorie=categorie_filtre)
    
    context = {
        'projets': tous_les_projets,
        'categories': categories,
        'categorie_selectionnee': categorie_filtre,
        'cv_actif': cv_actif,
    }
    return render(request, 'projets.html', context)

def detail_projet(request, pk):
    projet = get_object_or_404(Projet, pk=pk)
    cv_actif = CV.objects.filter(est_actif=True).first()
    context = {
        'projet': projet,
        'cv_actif': cv_actif,
    }
    return render(request, 'detail_projet.html', context)

def telecharger_cv(request):
    cv_actif = CV.objects.filter(est_actif=True).first()
    if cv_actif and cv_actif.fichier:
        try:
            fichier_cv = open(cv_actif.fichier.path, 'rb')
            response = FileResponse(fichier_cv, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="CV_Fils_Ngoma.pdf"'
            return response
        except:
            raise Http404("CV non disponible")
    else:
        messages.error(request, "Aucun CV disponible pour le moment.")
        return redirect('accueil')