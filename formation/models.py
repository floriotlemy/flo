from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=1000, verbose_name="Nom")

    def __str__(self):
        return self.nom 
    class Meta:
        verbose_name="Catégorie"
        verbose_name_plural="Catégories"
    
class Formation(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name="Catégorie")
    titre = models.CharField(max_length=2000,verbose_name="Titre")
    objectif = models.TextField(verbose_name="Objectfs")
    duree = models.CharField(max_length=50, verbose_name="Durée(jours)")
    tarif = models.IntegerField(verbose_name="Tarif par heure")
    prerequis = models.TextField(verbose_name="Prerequis")
    public = models.TextField(verbose_name="Public visé")

    def __str__(self):
        return self.titre 
    
