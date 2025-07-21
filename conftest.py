"""
Sets up the pytest testing environment.

Defines the API client fixture and test helpers fixture.
"""

import pytest

from client import ApiClient
from helpers import Helpers


@pytest.fixture(scope="module")
def api_client_fixture():
    """Supply an API client instance for the tests."""
    return ApiClient()


@pytest.fixture(scope="module")
def helpers_fixture(api_client_fixture):
    """
    Provide a Helpers instance for the tests.

    This fixture uses the api_client_fixture to send requests.
    """
    return Helpers(api_client_fixture)
