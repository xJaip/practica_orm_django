from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255, default='Desconocido')
    pais = models.CharField(max_length=255, default='Desconocido')
    
    def __str__(self):
        return self.nombre
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE, related_name='director_general')
    especialidad = models.CharField(max_length=255, default='Sin Especificar')
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='productos')
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)
    
    def __str__(self):
        return self.nombre
    