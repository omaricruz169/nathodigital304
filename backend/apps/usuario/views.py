from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, RegistroSerializer, UsuarioSerializer


def respuesta_con_token(user, codigo=status.HTTP_200_OK):
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'usuario': UsuarioSerializer(user).data}, status=codigo)


class RegistroView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Corregido: 'serailizer' a 'serializer'
        serializer = RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return respuesta_con_token(user, status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return respuesta_con_token(serializer.validated_data['user'])


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Corregido: 'dalete()' a 'delete()'
        Token.objects.filter(user=request.user).delete()
        return Response({'mensaje': 'Sesión cerrada.'})


class YoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UsuarioSerializer(request.user).data)