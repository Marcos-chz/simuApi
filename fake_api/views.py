from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Productos
from .serializers import ProductosSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else: 
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]