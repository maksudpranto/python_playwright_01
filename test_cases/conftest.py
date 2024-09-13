import pytest


@pytest.fixture()
def set_up_tear_down(page)->None:
    page.goto("https://saucedemo.com")
    yield page



