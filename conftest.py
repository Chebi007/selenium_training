import pytest
import jsonpickle
import os.path
import importlib
from fixture.application import Application

fixture = None


@pytest.fixture(scope="session")
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    fixture.session.login_on_admin_page(username="admin", password="admin")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(__file__), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())