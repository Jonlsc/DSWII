from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Categoria para filmes, séries e documentários
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Filmes
class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='filmes_imagens/')
    trailer = models.URLField()

    def __str__(self):
        return self.titulo

# Séries
class Serie(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    num_temporadas = models.IntegerField()
    imagem = models.ImageField(upload_to='series_imagens/')
    trailer = models.URLField()

    def __str__(self):
        return self.titulo

# Documentários
class Documentario(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    duracao = models.DurationField()
    imagem = models.ImageField(upload_to='documentarios_imagens/')
    trailer = models.URLField()

    def __str__(self):
        return self.titulo

# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O Email deve ser fornecido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    objects = UsuarioManager()

    def __str__(self):
        return self.email
