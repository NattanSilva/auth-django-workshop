from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny

from ..models import User
from .serializers import UserSerializer
from .permissions import IsAccountOwner


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAccountOwner]
    authentication_classes = [JWTAuthentication] 


class LoginViewset(viewsets.ViewSet):
    serializer_class = TokenObtainPairSerializer
    def create(self, request, *args, **kwargs):
        view = TokenObtainPairView.as_view()

        return view(request._request, *args, **kwargs)