from django.db import models
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Niveaux(models.Model):
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()


    def __str__(self):
        return self.nom
    
 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

class Matiere(models.Model):
    matiere_id = models.CharField(unique=True, max_length=40)
    nom = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE, related_name='matiere' )
    image = models.ImageField(upload_to='matiere', blank=True)
    description = models.TextField(max_length=500)


    def __str__(self):
        return self.nom
    
 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs)


class Lesson(models.Model):
    lesson_id = models.CharField(unique=True, max_length=40)
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    creer_par = models.ForeignKey(User, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='lesson')
    nom = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    position = models.PositiveSmallIntegerField(verbose_name='chapitre no')
    video = models.FileField(upload_to="video", null=True, blank=True, verbose_name="cours en video") 
    fpe = models.FileField(upload_to="FPE", null=True, blank=True, verbose_name="Une image du cours") 
    pdf = models.FileField(upload_to="PDF", null=True, blank=True, verbose_name="Fichier pdf du cours") 
    exercice = models.FileField(upload_to="PDF", null=True, blank=True, verbose_name="Fichier d'exercice d'application") 


    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.nom
    
 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("programmes:lessonlist", kwargs={"slug": self.matiere.slug, "niveau":self.niveau.slug})




"""EXERCICES
class Exercice(models.Model):
    exercice_id = models.CharField(unique=True, max_length=40)
    niveau = models.ForeignKey(Niveaux, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='exercices')
    nom = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(max_length=500)
    fichier = models.FileField(upload_to="exercices", null=True, blank=True, verbose_name="Fichier de l'exercice")

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("programmes:exercice_detail", kwargs={
            "niveau_slug": self.niveau.slug,
            "matiere_slug": self.matiere.slug,
            "lesson_slug": self.lesson.slug,
            "slug": self.slug
        })
"""

