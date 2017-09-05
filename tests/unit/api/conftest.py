import pytest
try:
    from unittest import mock
except ImportError:
    import mock


from wykop.api.clients import BaseWykopAPI
from wykop.api.v1.clients import WykopAPIv1, RotatingKeysWykopAPI
from wykop.api.exceptions.resolvers import ExceptionResolver


class Test1Exception(Exception):
    pass


class Test2Exception(Exception):
    pass


@pytest.fixture
def base_wykop_api():
    return BaseWykopAPI(
        mock.sentinel.appkey,
        mock.sentinel.secretkey,
        login=mock.sentinel.login,
        accountkey=mock.sentinel.accountkey,
        password=mock.sentinel.password,
        output=mock.sentinel.output,
        response_format=mock.sentinel.format,
    )


@pytest.fixture
def wykop_api():
    return WykopAPIv1(
        mock.sentinel.appkey,
        mock.sentinel.secretkey,
        output=mock.sentinel.output,
        response_format=mock.sentinel.format,
    )


@pytest.fixture
def key_pairs():
    return [
        (mock.sentinel.appkey1, mock.sentinel.secretkey1),
        (mock.sentinel.appkey2, mock.sentinel.secretkey2),
    ]


@pytest.fixture
def rotating_keys_wykop_api(key_pairs):
    return RotatingKeysWykopAPI(
        key_pairs,
        output=mock.sentinel.output,
        response_format=mock.sentinel.format,
    )


@pytest.fixture
def exception_resolver():
    exceptions = {
        1: Test1Exception,
        2: Test2Exception,
    }
    return ExceptionResolver(exceptions)
