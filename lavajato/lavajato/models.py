from django.db import models


class Cliente(models.Model):
    SEXO = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros')
    )
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=12)
    sexo = models.CharField(max_length=1, choices=SEXO, blank=False, null=False, default='O')

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    COR = (
        ('B', 'Branco'),
        ('P', 'Preto'),
        ('V', 'Vermelho'),
        ('A', 'Azul')
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    placa = models.CharField(max_length=7)
    ano = models.IntegerField()
    modelo = models.CharField(max_length=15)
    descricao = models.CharField(max_length=100)
    cor = models.CharField(max_length=1, choices=COR, blank=False, null=False, default='B')

    def __str__(self):
        return self.modelo

