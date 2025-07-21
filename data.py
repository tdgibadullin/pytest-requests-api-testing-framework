"""Defines the constants for the API request and response data."""


class JsonFields:
    """Stores the JSON field names for API requests and responses."""

    FIRST_NAME = "firstName"
    PHONE = "phone"
    ADDRESS = "address"
    AUTH_TOKEN = "authToken"
    CODE = "code"
    MESSAGE = "message"


class RequestData:
    """Stores the constant data for constructing API requests."""

    # The HTTP headers for a request, defining its body format as JSON.
    HEADERS = {"Content-Type": "application/json"}

    # The default user data for a user creation request body.
    USER_BODY = {
        JsonFields.FIRST_NAME: "Иван",
        JsonFields.PHONE: "+74441231234",
        JsonFields.ADDRESS: "г. Москва, ул. Большая Роща, д. 92"
    }


class StatusCodes:
    """Stores the expected API response status codes."""

    CREATED = 201
    BAD_REQUEST = 400


class Messages:
    """Stores the expected API response messages."""

    INVALID_FIRST_NAME_FORMAT = (
        "Имя пользователя введено некорректно. Имя может содержать только "
        "русские или латинские буквы, длина должна быть не менее 2 и не "
        "более 15 символов"
    )
    MISSING_PARAMETERS = "Не все необходимые параметры были переданы"
