from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nome da organização')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')
    company_registration_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='CNPJ')
    primary_contact_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Contato telefônico')
    primary_contact = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Responsável')


    class Meta:
        ordering = ['-created_at']
    def __str__(self) -> str:
        return self.name


class Department(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, verbose_name='Organização', related_name='departments')
    name = models.CharField(max_length=255, unique=True, verbose_name="Nome do departamento")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Data de atualização")
    company_registration_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="CNPJ"
    )
    primary_contact_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Contato telefônico"
    )
    primary_contact = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Responsável",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.name


class Division(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name="Departamento", related_name='units')
    name = models.CharField(max_length=255, unique=True, verbose_name="Nome da unidade")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Data de atualização")
    company_registration_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="CNPJ", default='SEM CADASTRO'
    )
    primary_contact_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Contato telefônico"
    )
    primary_contact = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Responsável",
    )

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:
        return self.name


class Sector(models.Model):
    division = models.ForeignKey(Division, on_delete=models.PROTECT, verbose_name='Unidade', related_name='sectors')
    name = models.CharField(max_length=255, unique=True, verbose_name='Nome do setor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')
    company_registration_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='CNPJ', default='SEM CADASTRO'
    )
    primary_contact_number = models.CharField(
        max_length=20, null=True, blank=True, verbose_name='Contato telefônico'
    )
    primary_contact = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Responsável",
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.name
