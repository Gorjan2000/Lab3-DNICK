from django.db import models
from django.contrib.auth.models import User


class BlogUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    naslov = models.CharField(max_length=30)
    avtor = models.ForeignKey(BlogUser, on_delete=models.CASCADE, null=True, blank=True)
    sodrzhina = models.CharField(max_length=50)
    fajlovi = models.ImageField(upload_to="data/", null=True, blank=True)
    datumKreiranje = models.DateField(auto_now_add=True)
    datumIzmena = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.naslov


class Komentari(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    komentator = models.ForeignKey(BlogUser, on_delete=models.CASCADE, null=True, blank=True)
    komentar = models.TextField(max_length=400)
    datumKreirano = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['datumKreirano']

    def __str__(self):
        return self.komentar[:60]


class Blokiran(models.Model):
    blokiran = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="blokiran")
    bloker = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="bloker")
