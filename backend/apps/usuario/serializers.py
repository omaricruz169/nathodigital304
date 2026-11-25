from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class UsuarioSerializer(serializers.ModelSerializer):
    usuario = serializers.CharField(source='username')
    nombre = serializers.CharField(source='first_name', max_length=60)

    class Meta:
        model = User
        fields = ['id', 'usuario', 'nombre']


class RegistroSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=60)
    usuario = serializers.RegexField(
        regex=r'^[a-zA-Z0-9.]{3,30}$',
        error_messages={'invalid': 'usa de 3 a 30 letras sin acentos, numeros, punto o guion bajo.'},
    )
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_usuario(self, valor):
        if User.objects.filter(username__iexact=valor).exists():
            raise serializers.ValidationError('Ese nombre de usuario ya está ocupado.')
        return valor

    def validate(self, datos):
        if datos['password'] != datos['password2']:
            raise serializers.ValidationError({'password2': 'Las contraseñas no coinciden.'})
        validate_password(datos['password'])
        return datos

    def create(self, datos):
        return User.objects.create_user(
            username=datos['usuario'],
            first_name=datos['nombre'],
            password=datos['password'],
        )


class LoginSerializer(serializers.Serializer):
    usuario = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, datos):
        user = authenticate(username=datos['usuario'], password=datos['password'])
        if user is None:
            raise serializers.ValidationError('Usuario o contraseña incorrecta.')
        datos['user'] = user
        return datos