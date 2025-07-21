"""
Implements the API client.

Encapsulates methods for retrieving and sending data via HTTP requests.
"""

import requests

from configuration import ApiConfig
from data import RequestData


class ApiClient:
    """The client for interacting with the API."""

    def __init__(self):
        """Initialize the API client with the base URL and headers."""
        self.base_url = ApiConfig.BASE_URL
        self.headers = RequestData.HEADERS

    def get_users_table(self):
        """Send a GET request to receive data from the Users table."""
        full_url = f"{self.base_url}{ApiConfig.USERS_TABLE_PATH}"
        return requests.get(full_url, timeout=ApiConfig.REQUEST_TIMEOUT)

    def post_new_user(self, body):
        """
        Send a POST request to create a new user.

        The request is sent with the given body.
        """
        full_url = f"{self.base_url}{ApiConfig.CREATE_USER_PATH}"
        return requests.post(
            full_url,
            json=body,
            headers=self.headers,
            timeout=ApiConfig.REQUEST_TIMEOUT
        )
