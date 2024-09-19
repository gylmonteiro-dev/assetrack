from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from registry_entities.models import Sector


TYPE_OPTIONS = (('MOBILE', 'MOVÉL'),
                   ('IMOBILE', 'IMÓVEL'))


CONDITION_OPTIONS = (('NEW', 'NOVO'),
                     ('USED', 'USADO'),
                     ('DAMAGED', 'DANIFICADO'))

AVAILABILITY_OPTIONS = (('IN USE', 'EM USO'),
                        ('IN STOCK', 'EM ESTOQUE'),
                        ('IN REPAIR', 'EM MANUTENÇÃO'),
                        ('UNAVAILABLE', 'INDISPONÍVEL'))

# Create your models here.
class CostCenter(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome do centro de custo')
    details = models.TextField(null=True, blank=True, verbose_name='detalhes do centro de custo')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome da categoria')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data do registro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização do registro')

    def __str__(self):
        return self.name


class Asset(models.Model):
    # sector = models.ForeignKey(Sector, on_delete=models.PROTECT, verbose_name='Setor', related_name='ativos')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoria', related_name='ativos')
    name = models.CharField(max_length=255, verbose_name='Nome')
    model = models.CharField(max_length=100, null=True, blank=True, verbose_name='Modelo')
    serial_number = models.CharField(max_length=100, blank=True, null=True, verbose_name='Número de série')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Preço')
    warranty = models.DateField(null=True, blank=True)
    invoice_number = models.CharField(max_length=100, verbose_name='Nota fiscal')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    condition = models.CharField(max_length=10, choices=CONDITION_OPTIONS, default='USED', verbose_name='Condição')
    type = models.CharField(max_length=10, choices=TYPE_OPTIONS, default='MOBILE')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data do registro")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de atualização do registro")

    def __str__(self):
        return  self.name


class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome do fornecedor')
    company_registration_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='CNPJ', default='SEM CADASTRO')
    person_registration_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='CPF', default='SEM CADASTRO')

    def __str__(self):
        return self.name

class RegisterAsset(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário', related_name='registros_de_ativos')
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, verbose_name='Ativo', related_name='registros_de_ativos')
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, verbose_name='Setor', related_name='registro_de_ativos')
    cost_center = models.ForeignKey(CostCenter, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Centro de custo', related_name='registros_de_ativos')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Fornecedor', related_name='registros_de_ativos')
    amount = models.IntegerField(validators=[MinValueValidator(1, 'Não pode cadastrar com quantidade menor que 1')])
    observation = models.TextField(null=True, blank=True, verbose_name='Observação')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    availability = models.CharField(max_length=50, choices=AVAILABILITY_OPTIONS, verbose_name='Disponibilidade', null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def __str__(self) -> str:
        return f"{self.asset}: {self.sector}"
