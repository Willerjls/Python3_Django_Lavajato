from rest_framework import viewsets
from lavajato.models import Cliente, Veiculo, Venda
from lavajato.serializer import ClienteSerializer, VeiculoSerializer, VendaSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VeiculosViewSets(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class VendaViewSets(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
