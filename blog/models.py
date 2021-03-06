from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Article(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(verbose_name="Date de parution",
                                auto_now_add=True, auto_now=False)
    is_visible = models.BooleanField(verbose_name="Article publié ?",
                                     default=False)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    def __str__(self):
        return self.titre


class Comment(models.Model):
    """ Modèle pour les commentaires """
    pseudo = models.CharField(max_length=42)
    email = models.EmailField(max_length=254)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    contenu = models.TextField(null=False, verbose_name="Description")
    is_visible = models.BooleanField(verbose_name="Commentaire visible ?",
                                    default=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.pseudo
