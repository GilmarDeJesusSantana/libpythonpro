from unittest.mock import Mock

import pytest

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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'gilmar@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantáticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Gilmar', email='gilmar@gmail.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'santana@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with == (
        'santana@gmail.com',
        'gilmar@gmail.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
