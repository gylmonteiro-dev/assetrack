# Generated by Django 5.1.1 on 2024-09-19 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_patrimony', '0002_registerasset_availability'),
        ('registry_entities', '0003_alter_division_company_registration_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerasset',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registros_de_ativos', to='registry_entities.sector', verbose_name='Setor'),
        ),
    ]
