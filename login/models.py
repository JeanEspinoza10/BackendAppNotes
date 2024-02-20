from django.db import models
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser



# Create your models here.

'''
Create custom model 

'''

class RolApp(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.name

class UserApp(AbstractUser):
    
    '''
    Recordar: al ser un modelo personalizado, no olvidarse de crear 
    la variable en settings del proyecto: AUTH_USER_MODEL.
    '''
    email = models.EmailField(unique=True)
    status = models.BooleanField(default=True)
    phone = models.CharField(max_length=100,blank=True)

    '''
    Creamos los campos para que obtener la fechas:
        create => auto_now_add solamente la primera vez
        update => para cualquier acción
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    rol_id = models.ForeignKey(RolApp, on_delete=models.PROTECT, null=True)
    
    class Meta:
        ordering = ['id']
        db_table = 'usersapp'
    
    
    
    '''
    Campos requeridos para validarse con el usermanager
    '''
    REQUIRED_FIELDS = ['email', 'password']

    



