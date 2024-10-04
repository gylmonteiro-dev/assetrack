# Generated by Django 5.1.1 on 2024-09-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management_patrimony", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="registerasset",
            name="availability",
            field=models.CharField(
                blank=True,
                choices=[
                    ("IN USE", "EM USO"),
                    ("IN STOCK", "EM ESTOQUE"),
                    ("IN REPAIR", "EM MANUTENÇÃO"),
                    ("UNAVAILABLE", "INDISPONÍVEL"),
                ],
                max_length=50,
                null=True,
                verbose_name="Disponibilidade",
            ),
        ),
    ]
