"""
Defines the base URL, API endpoint paths and timeout used in requests.

Used by the API client to construct full request URLs and set timeouts.
"""


class ApiConfig:
    """Stores the base URL, API endpoint paths and requests timeout."""

    # The base URL for the Yandex.Prilavok API.
    # Note: this is a sample URL used in this framework.
    # It is dynamically generated and temporary, currently inaccessible.
    BASE_URL = (
        "https://eca5334b-2082-462f-a753-3cc5c3a51c6a."
        "serverhub.praktikum-services.ru"
    )

    # The API endpoint path for creating a new user.
    CREATE_USER_PATH = "/api/v1/users/"

    # The API endpoint path for the Users (user data) table.
    USERS_TABLE_PATH = "/api/db/resources/user_model.csv"

    # The timeout (in seconds) for API requests.
    REQUEST_TIMEOUT = 10
