from rest_framework import serializers
from lavajato.models import Cliente, Veiculo


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'


class ListaVeiculosClienteSerializer(serializers.ModelSerializer):
    cor = serializers.SerializerMethodField()

    class Meta:
        model = Veiculo
        fields = '__all__'

    def get_cor(self, obj):
        return obj.get_cor_display()
