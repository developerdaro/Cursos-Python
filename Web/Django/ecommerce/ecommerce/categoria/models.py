from django.db import models

# Create your models here.
class Categoria(models.Model):
    categoria_nombre=models.CharField(max_length=50,unique=True)
    descripcion=models.CharField(max_length=255,blank=True)
    slug=models.CharField(max_length=100,unique=True) #concepto para estar en la parte final de la url que representa la identidad
    categoria_imagen=models.ImageField(upload_to='fotos/categorias', blank=True)


    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias" #Forma para visualizar en el admin si es plural

    def __str__(self):
        return self.categoria_nombre
