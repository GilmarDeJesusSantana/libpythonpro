import pytest

from libpythonpro.spam.enviador_email import Enviador


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None
@pytest.mark.parametrize(
    'destinatario',
    ['gilmar.jesus@gmail.com','foo.bar@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado=enviador.enviar(
        destinatario,
        'gilmar.jesus@gmail.com',
        'Curso Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert destinatario in resultado