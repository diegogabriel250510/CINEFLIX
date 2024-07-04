from django.db import models

# Create your models here.
class Imagem(models.Model):
    img = models.ImageField(upload_to='img')

    def __str__(self) -> str:
        return self.img.url

class Filme(models.Model):
    choices = (('DR', 'drama'),
               ('C', 'comedia'),
               ('R', 'romance'),
               ('DOC', 'documentario'),
               ('AC', 'ação'),
               ('AV', 'aventura'),
               ('FC', 'ficção cientifica'),
               ('T', 'Terror'))
    nome = models.CharField(max_length=50)
    onde_assistir = models.CharField(max_length=50)
    categoria = models.CharField(max_length=3, choices=choices)
    descricao = models.TextField()

    def __str__(self):
        return self.nome