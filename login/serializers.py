from rest_framework import serializers
from login.models import UserApp
from .models import UserApp, RolApp


class UserSerializer(serializers.ModelSerializer):
    '''
    Serializador para nuestro modelo UserApp
    '''
    class Meta:
        model = UserApp
        exclude = ['password']



class UserCreateSerializer(serializers.ModelSerializer):
    confirmation_password = serializers.CharField(max_length=128, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    class Meta:
        model = UserApp
        fields = ['username','password','confirmation_password','email','first_name','last_name','phone']


    '''
    Funcion para realizar propias validaciones, la funcion debe tener
    validate_(nombre de la variable a validar)
    '''
    def validate_confirmation_password(self,value):
        values = self.get_initial()
        if value != values.get('password'):
            raise serializers.ValidationError('password are not the same')
        return value


    '''
    Accion del metodo save() => se modifica por este metodo
    '''
    def create(self, validated_data):
        '''
        Por defecto siempre se tiene el rol usuario para la creación de nuevos usuarios.
        '''
        rol_instance = RolApp.objects.get(name='usuario')
        
        validated_data.pop('confirmation_password')
        validated_data['rol_id'] = rol_instance
        return UserApp.objects.create_user(**validated_data)