from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import path

'''
Personalizar el swagger
'''
views = get_schema_view(    
    openapi.Info(
        title='ApiRest Todolist',
        default_version='1.0',
        description= 'Documentación'
    ),
    permission_classes=[permissions.AllowAny]

)

urlpatterns = [
    path('swagger-ui/',views.with_ui('swagger'), name='swagger-ui'),
    path('redoc/',views.with_ui('swagger'),name='redoc')
]