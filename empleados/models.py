from django.db import models
from departamento.models import Departamento

# Create your models here.

class Empleado(models.Model):
    JOB_CHOICES = [
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),        
        ('3', 'Otro'),        
    ]
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #image = models.ImageField('Image', upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' ' + self.last_name
    
