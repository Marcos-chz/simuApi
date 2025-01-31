from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Productos
from .serializers import ProductosSerializer
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator

error_mensage = "The elements from 1 to 6 cannot be modified or eliminated."


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

    @method_decorator(ratelimit(key='ip', rate='5/m', block=True))
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        producto = self.get_object()
        
        # Verificar si el producto está protegido
        if producto.is_default:
            return Response(
                {"error": error_mensage},
                status=status.HTTP_403_FORBIDDEN
            )
        #super llama al metodo de la clase (ModelViewset)
        return super().destroy(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        producto = self.get_object()
        
        # Verificar si el producto está protegido
        if producto.is_default:
            return Response(
                {"error": error_mensage},
                status=status.HTTP_403_FORBIDDEN
            )
        
        return super().update(request, *args, **kwargs)