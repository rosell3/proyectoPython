from django.db import models

# Create your models here.
class pokemon(models.Model):
    codigo = models.CharField(max_length=45, null=False, unique=True)
    nombre = models.CharField(max_length=150, null=False)
    elemento = models.CharField(max_length=150, null=False)
    genero = models.CharField(max_length=150, null=False)
    estado = models.CharField(max_length=150, null=False)


# Create your models here.
