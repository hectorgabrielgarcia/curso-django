from django.db import models

# Create your models here.
class contactos (models.Model):
    nombre=models.CharField(max_length=100)
    segundonombre=models.CharField(max_length=100 , null=True, blank = True)
    apellidomaterno=models.CharField(max_length=100)
    apelludopaterno=models.CharField(max_length=100)

    telcasa=models.CharField(max_length=100, null=True, blank = True)
    celular=models.CharField(max_length=100)
    email=models.EmailField()
    twitter=models.URLField(null=True, blank = True)
    paginaweb=models.URLField(null=True, blank = True)

    created=models.DateTimeField(auto_now_add = True)
    updated=models.DateTimeField(auto_now = True) #cada que se modifique se modifica la fecha y hora automatico

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
        ordering=['id']
    
    def __str__(self):
        return '%s %s' % (self.apelludopaterno,self.nombre)