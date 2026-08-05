import pytest
from test_damashka_7.sandbox_1_api import SandBoxApi

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture
def api():
    return SandBoxApi(BASE_URL)


@pytest.fixture
def auth_token(api):
    """Фикстура для получения токена перед тестами, требующими прав"""
    return api.get_auth_token("admin", "password123")


@pytest.fixture
def sample_booking_data():
    return {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-10"
        },
        "additionalneeds": "Breakfast"
    }


def test_create_booking(api, sample_booking_data):
    """Тест на создание бронирования"""
    response_data = api.create_booking(sample_booking_data)

    assert "bookingid" in response_data
    assert response_data["booking"]["firstname"] == sample_booking_data["firstname"]
    assert response_data["booking"]["lastname"] == sample_booking_data["lastname"]
    assert response_data["booking"]["totalprice"] == sample_booking_data["totalprice"]


def test_partial_update_booking(api, auth_token, sample_booking_data):
    """Тест на частичное изменение бронирования (PATCH)"""
    created_booking = api.create_booking(sample_booking_data)
    booking_id = created_booking["bookingid"]

    update_data = {
        "firstname": "anna",
        "lastname": "korovina"
    }

    response = api.partial_update_booking(booking_id, update_data, auth_token)

    assert response.status_code == 200
    updated_json = response.json()
    assert updated_json["firstname"] == "anna"
    assert updated_json["lastname"] == "korovina"
    assert updated_json["totalprice"] == sample_booking_data["totalprice"]


def test_negative_get_nonexistent_booking(api):
    """Негативный сценарий: попытка получить несуществующее бронирование"""
    non_existent_id = -1
    response = api.get_booking(non_existent_id)
    assert response.status_code == 404