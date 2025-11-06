from django.db import models

class CV(models.Model):
    fichier = models.FileField(upload_to='cv/')
    date_upload = models.DateTimeField(auto_now_add=True)
    est_actif = models.BooleanField(default=True)

    def __str__(self):
        return f"CV - {self.date_upload.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = "CV"
        verbose_name_plural = "CV"

class Competence(models.Model):
    nom = models.CharField(max_length=100)
    pourcentage = models.IntegerField()
    categorie = models.CharField(max_length=50)
    icone = models.CharField(max_length=50, default='fas fa-code')

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"

class Projet(models.Model):
    CATEGORIE_CHOICES = [
        ('web', 'Développement Web'),
        ('mobile', 'Développement Mobile'),
        ('design', 'Design Graphique'),
    ]
    
    titre = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projets/')
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    technologies = models.CharField(max_length=200)
    url_projet = models.URLField(blank=True)
    url_github = models.URLField(blank=True)
    date_realisation = models.DateField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-date_realisation']

class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    email_verifie = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"