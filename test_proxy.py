import requests
import pytest

from conf import *


def test_proxy():
    resp = requests.get(PROXY_TEST_URL, proxies=PROXY)
    expected = PROXY['https'].split(':')[1]
    output = resp.json()
    assert expected == output