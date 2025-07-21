"""
Defines helper methods for the tests.

Covers generating request bodies and asserting responses.
"""

from data import JsonFields, RequestData, StatusCodes, Messages


class Helpers:
    """Contains test helper methods."""

    def __init__(self, api_client):
        """Initialize the test helpers with an API client instance."""
        self.api_client = api_client

    @staticmethod
    def get_user_body(first_name):
        """
        Generate a request body with the given firstName value.

        If first_name is 'missing', the firstName field is removed.
        Otherwise, it is set to the provided value.
        """
        current_body = RequestData.USER_BODY.copy()

        if first_name == "missing":
            current_body.pop(JsonFields.FIRST_NAME)
        else:
            current_body[JsonFields.FIRST_NAME] = first_name

        return current_body

    def positive_assert(self, first_name):
        """
        Assert user creation with the given valid firstName value.

        Checks for the 201 status code and presence of an auth token.
        Ensures the user data appears exactly once in the Users table.
        """
        user_body = self.get_user_body(first_name)
        user_response = self.api_client.post_new_user(user_body)

        assert user_response.status_code == StatusCodes.CREATED
        assert user_response.json()[JsonFields.AUTH_TOKEN] != ""

        users_table_response = self.api_client.get_users_table()
        expected_user_string = (
            f"{user_body[JsonFields.FIRST_NAME]},"
            f"{user_body[JsonFields.PHONE]},"
            f"{user_body[JsonFields.ADDRESS]},"
            f",," # Optional empty "email" and "comment" fields
            f"{user_response.json()[JsonFields.AUTH_TOKEN]}"
        )

        assert users_table_response.text.count(expected_user_string) == 1

    def negative_assert_invalid_first_name_format(self, first_name):
        """
        Assert the error for the given invalid format firstName value.

        Checks for the 400 status code and expected response fields.
        """
        user_body = self.get_user_body(first_name)
        response = self.api_client.post_new_user(user_body)

        assert response.status_code == StatusCodes.BAD_REQUEST
        assert response.json()[JsonFields.CODE] == StatusCodes.BAD_REQUEST
        assert response.json()[JsonFields.MESSAGE] == (
            Messages.INVALID_FIRST_NAME_FORMAT
        )

    def negative_assert_no_first_name(self, user_body):
        """
        Assert the error for the given null/empty value or missing field.

        Checks for the 400 status code and expected response fields.
        """
        response = self.api_client.post_new_user(user_body)

        assert response.status_code == StatusCodes.BAD_REQUEST
        assert response.json()[JsonFields.CODE] == StatusCodes.BAD_REQUEST
        assert response.json()[JsonFields.MESSAGE] == (
            Messages.MISSING_PARAMETERS
        )

    def negative_assert_non_string_first_name(self, first_name):
        """
        Assert the error for the given non-string type firstName value.

        Checks for the 400 status code.
        """
        user_body = self.get_user_body(first_name)
        response = self.api_client.post_new_user(user_body)

        assert response.status_code == StatusCodes.BAD_REQUEST
