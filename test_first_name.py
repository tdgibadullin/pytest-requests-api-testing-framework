"""
Test module for the API user creation endpoint.

Covers validation of the firstName field in the request body.
"""

import pytest


class TestFirstName:
    """
    Tests for the firstName field when creating a user.

    Note: test numeration matches the checklist item numbers.
    """

    @pytest.mark.parametrize(
        "first_name", [
            pytest.param("Ив", id="1: 2 chars"),
            pytest.param("Ива", id="2: 3 chars"),
            pytest.param("ИванИванИв", id="3: 10 chars"),
            pytest.param("ИванИванИванИв", id="4: 14 chars"),
            pytest.param("ИванИванИванИва", id="5: 15 chars"),
            pytest.param("Ivan", id="6: English chars"),
            pytest.param("Жак-Ив", id="7: Hyphen"),
        ]
    )
    def test_user_creation_with_valid_first_name_succeeds(
            self,
            first_name,
            helpers_fixture
    ):
        """Verify user creation with a valid firstName value."""
        helpers_fixture.positive_assert(first_name)

    @pytest.mark.parametrize(
        "first_name", [
            pytest.param("И", id="8: 1 char"),
            pytest.param("ИванИванИванИван", id="9: 16 chars"),
            pytest.param("ИванИванИванИванИван", id="10: 20 chars"),
            pytest.param("И" * 300, id="11: 300 chars"),
            pytest.param(
                " Иван",
                marks=pytest.mark.xfail(
                    reason="API allows spaces, got 201, expected error 400"
                ),
                id="12: Leading space"
            ),
            pytest.param(
                "Ив ан",
                marks=pytest.mark.xfail(
                    reason="API allows spaces, got 201, expected error 400"
                ),
                id="13: Middle space"
            ),
            pytest.param(
                "Иван ",
                marks=pytest.mark.xfail(
                    reason="API allows spaces, got 201, expected error 400"
                ),
                id="14: Trailing space"
            ),
            pytest.param("Иван@", id="15: Special char"),
            pytest.param("Иван1", id="16: Digit"),
        ]
    )
    def test_user_creation_with_invalid_first_name_format_fails(
            self,
            first_name,
            helpers_fixture
    ):
        """Verify the error for an invalid firstName value format."""
        helpers_fixture.negative_assert_invalid_first_name_format(
            first_name
        )

    @pytest.mark.parametrize(
        "first_name", [
            pytest.param(
                None,
                id="17: Value is null (None)"
            ),
            pytest.param(
                "",
                id="18: Empty value"
            ),
            pytest.param(
                "missing",
                id="19: Missing field"
            ),
        ]
    )
    def test_user_creation_with_no_first_name_fails(
            self,
            first_name,
            helpers_fixture
    ):
        """
        Verify the error when the firstName value is absent.

        Covers null/empty value and missing field cases.
        """
        user_body = helpers_fixture.get_user_body(first_name)
        helpers_fixture.negative_assert_no_first_name(user_body)

    @pytest.mark.xfail(reason="API returns 500 for integer, expected 400")
    def test_user_creation_with_integer_first_name_fails(
            self,
            helpers_fixture
    ):
        """
        Verify the error when the firstName value is an integer.

        Test #20.
        """
        helpers_fixture.negative_assert_non_string_first_name(12)
