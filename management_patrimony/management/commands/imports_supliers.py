import csv
from django.core.management.base import BaseCommand
from management_patrimony.models import Supplier


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo de fornecedores'
        )


    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                nome = row['nome_do_fornecedor']
                cnpj = row['cnpj']
                cpf = row['cpf']

                self.stdout.write(self.style.NOTICE(nome))
                Supplier.objects.create(name=nome, company_registration_number=cnpj, person_registration_number=cpf)

            self.stdout.write(self.style.SUCCESS('Forncedores cadastrados com sucesso'))