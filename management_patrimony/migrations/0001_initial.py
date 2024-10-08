# Generated by Django 5.1.1 on 2024-09-19 11:51

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        (
            "registry_entities",
            "0003_alter_division_company_registration_number_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Nome da categoria"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data do registro"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de atualização do registro"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CostCenter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, verbose_name="Nome do centro de custo"
                    ),
                ),
                (
                    "details",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="detalhes do centro de custo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Nome do fornecedor"),
                ),
                (
                    "company_registration_number",
                    models.CharField(
                        blank=True,
                        default="SEM CADASTRO",
                        max_length=20,
                        null=True,
                        verbose_name="CNPJ",
                    ),
                ),
                (
                    "person_registration_number",
                    models.CharField(
                        blank=True,
                        default="SEM CADASTRO",
                        max_length=20,
                        null=True,
                        verbose_name="CPF",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Asset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Nome")),
                (
                    "model",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Modelo"
                    ),
                ),
                (
                    "serial_number",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Número de série",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Preço",
                    ),
                ),
                ("warranty", models.DateField(blank=True, null=True)),
                (
                    "invoice_number",
                    models.CharField(max_length=100, verbose_name="Nota fiscal"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Descrição"),
                ),
                (
                    "condition",
                    models.CharField(
                        choices=[
                            ("NEW", "NOVO"),
                            ("USED", "USADO"),
                            ("DAMAGED", "DANIFICADO"),
                        ],
                        default="USED",
                        max_length=10,
                        verbose_name="Condição",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("MOBILE", "MOVÉL"), ("IMOBILE", "IMÓVEL")],
                        default="MOBILE",
                        max_length=10,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data do registro"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de atualização do registro"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="ativos",
                        to="management_patrimony.category",
                        verbose_name="Categoria",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RegisterAsset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, "Não pode cadastrar com quantidade menor que 1"
                            )
                        ]
                    ),
                ),
                (
                    "observation",
                    models.TextField(blank=True, null=True, verbose_name="Observação"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de criação"
                    ),
                ),
                (
                    "update_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de atualização"
                    ),
                ),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="registros_de_ativos",
                        to="management_patrimony.asset",
                        verbose_name="Ativo",
                    ),
                ),
                (
                    "cost_center",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="registros_de_ativos",
                        to="management_patrimony.costcenter",
                        verbose_name="Centro de custo",
                    ),
                ),
                (
                    "sector",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="registro_de_ativos",
                        to="registry_entities.sector",
                        verbose_name="Setor",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="registros_de_ativos",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="registros_de_ativos",
                        to="management_patrimony.supplier",
                        verbose_name="Fornecedor",
                    ),
                ),
            ],
        ),
    ]
