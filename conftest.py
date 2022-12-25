import json
import pytest
from random import choice

from api_framework.CONSTANS import ROOT_DIR
from api_framework.data.booking import Booking
from api_framework.data.booking_data import BookingData
from api_framework.utilites.configuration import Configuration
from api_framework.API_colection.booking_api_colections import BookingAPI


@pytest.fixture(scope='session')
def environment():
    with open(f'{ROOT_DIR}/configuration.json') as f:
        data = f.read()
        json_to_dict = json.loads(data)
    config = Configuration(**json_to_dict)
    return config


@pytest.fixture()
def create_booking(environment):
    get_all_bookings = BookingAPI(environment).get_all_bookings()
    booking_id = choice([number["bookingid"] for number in json.loads(get_all_bookings.text)])
    response = BookingAPI(environment).get_booking_by_id(booking_id)
    json_to_dict = json.loads(response.text)
    bookings_data = {'bookingid': booking_id, "booking": json_to_dict}
    test_booking = Booking(**bookings_data)
    return test_booking


@pytest.fixture()
def get_instance_booking_id(environment):
    get_all_bookings = BookingAPI(environment).get_all_bookings()
    bookings_id = choice([number["bookingid"] for number in json.loads(get_all_bookings.text)])
    return bookings_id


@pytest.fixture()
def expected_booking_data():
    return BookingData()
