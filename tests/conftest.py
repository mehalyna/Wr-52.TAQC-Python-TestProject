# Pytest configuration file
# See https://docs.pytest.org/en/latest/ for more information

import pytest


@pytest.fixture(scope="session")
def scope_method():
    pass
