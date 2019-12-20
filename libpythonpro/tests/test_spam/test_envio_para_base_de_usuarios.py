import pytest

from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Santana', email='santana@gmail.com'),
            Usuario(nome='Gilmar', email='gilmar@gmail.com.br')
        ],
        [
            Usuario(nome='Gilmar', email='gilmar@gmail.com.br')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gilmar@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantáticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gilmar', email='gilmar@gmail.com.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'santana@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'santana@gmail.com',
        'gilmar@gmail.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
