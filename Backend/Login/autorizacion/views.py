from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer

class VistaProtected(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    def get(self, request):
        groups = request.user.groups.values_list('name', flat = True)
        print(groups[0])
        return Response({"info" : self.serializer_class(request.user).data, "groups": str(groups[0])})


class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        # Extraer credenciales del request
        username = request.data.get("username")
        password = request.data.get("password")
        
        # Autenticar usuario
        user = authenticate(username=username, password=password)

        if user is not None:
            # Generar o recuperar el token
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "message": "Login exitoso", "userinfo": self.serializer_class(user).data})
        else:
            # Enviar un error si las credenciales no son válidas
            return Response({"error": "Credenciales inválidas, Kill yourself"}, status=400)
        
