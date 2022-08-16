################################################################
# Usage of conftest.py
# https://stackoverflow.com/questions/34466027/in-py-test-what-is-the-use-of-conftest-py-files
import pytest


################################################################
# 1. Fixture
################################################################


@pytest.fixture()
def env(request):
    return request.config.getoption("--env")

@pytest.fixture()
def scope(request):
    for marker in request.node.own_markers:
        if marker.name in ['uat', 'rat', 'fast', 'toft']:
            return marker.name

@pytest.fixture()
def endpoint(request, env):
    """Return a base URL"""
    config = request.config
    url = config.getoption('endpoint')
    if url is not None:
        return url

    api_endpoint = {
        'dev': 'https://api.dev.illusory.one',
        'staging': 'https://api.staging.illusory.one',
        'production': 'https://api.illusory.one',
    }

    if env:
        return api_endpoint[env]

    return 'https://127.0.0.1'

def pytest_addoption(parser):
    parser.addoption('--env', default="dev", help="environment")
    parser.addoption('--endpoint', default=None, help='endpoint of api server')
