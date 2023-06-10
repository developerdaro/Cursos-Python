from django.db import models

# Create your models here.
class Usuario(models.Model):

    genero_eleccion=(
    ('M','Masculino'),
    ('F','Femenino'),
    )

    codigo=models.IntegerField()
    foto=models.ImageField(upload_to="fotos/%Y/%m/%d/")#Para que almacene la foto en carpetas ordenadas por año-mes-dia
    nombre=models.CharField(max_length=100)
    profesion=models.CharField(max_length=100)
    genero=models.CharField(choices=genero_eleccion,max_length=100)
    ciudad=models.CharField(max_length=100)


    def __str__(self):
        return self.nombre
