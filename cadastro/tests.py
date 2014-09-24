from django.test import TestCase
from django.core.urlresolvers import reverse
from cadastro.models import Paciente

class PacientTestCase(TestCase):

    def test_create_paciente_by_model(self):
        paciente = Paciente(
            numero_paciente= 1,
            data_registro= '2014-09-23',
            nome= 'victor',
            sexo= 'M',
            data_nascimento= '1986-05-14',
            nome_mae= 'Tania',
            cep= '23742324',
            endereco= 'rua',
            numero= '123',
            complemento= 'complemento',
            bairro= 'chácara',
            cidade= 'Petrópolis',
            uf= 'RJ',
            rg= '20437438',
            cpf= '2384234',
            telefone= '2343534',
            celular= '3847653',
            convenio_sus= 'N',
            numero_sus= '28343',
            email='vtm@hot.com',
            informacao_menor= 'blblb'
        )
        paciente.save()
        self.assertEqual(paciente.pk, 1)

    def test_create_paciente_by_view(self):
        data = {
            'numero_paciente': 2,
            'data_registro': '2014-09-23',
            'nome': 'victor2',
            'sexo': 'M',
            'data_nascimento': '1986-05-14',
            'nome_mae': 'Tania',
            'cep': '23742324',
            'endereco': 'rua',
            'numero': '123',
            'complemento': 'complemento',
            'bairro': 'chácara',
            'cidade': 'Petrópolis',
            'uf': 'RJ',
            'rg': '20437438',
            'cpf': '2384234',
            'telefone': '2343534',
            'celular': '3847653',
            'convenio_sus': 'N',
            'numero_sus': '28343',
            'email': 'vtm2@hot.com',
            'informacao_menor': '2blblb'
        }

        response = self.client.post(reverse('paciente_new'), data, format='JSON')
        self.assertEqual(response.status_code, 201)

