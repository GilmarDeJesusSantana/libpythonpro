from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars3.githubusercontent.com/u/33839314?v=4'
    resp_mock.json.return_value = {
        "login": "GilmarDeJesusSantana", "id": 33839314,
        "avatar_url": url,
    }
    github_api_original = github_api.request.get()
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = github_api_original

def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('GilmarDeJesusSantana')
    assert avatar_url == url

def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('GilmarDeJesusSantana')
    assert 'https://avatars3.githubusercontent.com/u/33839314?v=4' == url
