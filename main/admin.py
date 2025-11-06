from django.contrib import admin
from .models import Competence, Projet, MessageContact, CV

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ['fichier', 'date_upload', 'est_actif']
    list_editable = ['est_actif']

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ['nom', 'pourcentage', 'categorie']
    list_filter = ['categorie']

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ['titre', 'categorie', 'date_realisation']
    list_filter = ['categorie', 'date_realisation']
    search_fields = ['titre', 'description']

@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ['nom', 'email', 'sujet', 'date_envoi']
    readonly_fields = ['date_envoi']