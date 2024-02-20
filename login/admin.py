from django.contrib import admin
from .models import UserApp, RolApp
# Register your models here.

'''
Register my models
'''

'''
Personalizar las vistas en el administrador
'''
@admin.register(UserApp)
class UserAppAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','phone','status','rol_id']
    search_fields = ['email']
    list_filter = ['status']

@admin.register(RolApp)
class RolAppAdmin(admin.ModelAdmin):
    list_display = ['id','name']