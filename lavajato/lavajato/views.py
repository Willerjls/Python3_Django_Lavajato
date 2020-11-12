from rest_framework import viewsets
from lavajato.models import Cliente, Veiculo
from lavajato.serializer import ClienteSerializer, VeiculoSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VeiculosViewSets(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
