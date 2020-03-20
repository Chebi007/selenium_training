import pytest
from fixture.application import Application

fixture = None


@pytest.fixture(scope="session")
def app():
    global fixture
    if fixture is None:
        fixture = Application()
    fixture.session.login(username="admin", password="admin")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
