import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.fixture
def products() -> list[dict]:
    return [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]


@pytest.mark.parametrize("today_date,result", [
    (
        datetime.date(2022, 2, 1),
        []
    ),
    (
        datetime.date(2022, 2, 2),
        ["duck"]
    ),
    (
        datetime.date(2022, 2, 2),
        ["duck"]
    ),
    (
        datetime.date(2022, 2, 6),
        ["chicken", "duck"]
    ),
    (
        datetime.date(2022, 2, 10),
        ["chicken", "duck"]
    ),
    (
        datetime.date(2022, 2, 11),
        ["salmon", "chicken", "duck"]
    )
])
@mock.patch("datetime.date")
def test_should_return_outdated_products_when_date_is(
        mock_today_date: type[datetime],
        products: list[dict],
        today_date: type[datetime],
        result: list[str]
) -> None:
    mock_today_date.today.return_value = today_date
    assert outdated_products(products) == result
