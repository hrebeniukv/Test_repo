import random
import json
from api_framework.data.booking import Booking
from api_framework.API_colection.booking_api_colections import BookingAPI
from http import HTTPStatus
import time
from api_framework.data.booking_data import BookingData


def test_get_booking_by_id(environment, get_instance_booking_id):
    booking_id = get_instance_booking_id
    response = BookingAPI(environment).get_booking_by_id(booking_id)
    assert response.status_code == HTTPStatus.OK


def test_get_booking_by_unexist_id(environment):
    get_all_bookings = BookingAPI(environment).get_all_bookings()
    bookings_list = sorted([number["bookingid"] for number in json.loads(get_all_bookings.text)])
    response = BookingAPI(environment).get_booking_by_id(bookings_list[-1] + 2)
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_id_of_new_booking(environment, get_instance_booking_id):
    """response = BookingAPI(environment).create_new_booking()
    booking_id = json.loads(response.text)]["bookingid"]"""
    booking_id = get_instance_booking_id
    get_all_bookings = BookingAPI(environment).get_all_bookings()
    bookings_list = [number["bookingid"] for number in json.loads(get_all_bookings.text)]
    assert booking_id in bookings_list


def test_checking_of_new_customer(environment, create_booking):
    """response = BookingAPI(environment).create_new_booking()
    actual_booking = Booking(**json.loads(response.text))"""
    expected_booking = create_booking
    booking_id = expected_booking.bookingid
    response = BookingAPI(environment).get_booking_by_id(booking_id)
    booking_data = json.loads(response.text)
    data = {'bookingid': booking_id, "booking": booking_data}
    actual_booking = Booking.from_json(**data)
    assert expected_booking == actual_booking


def test_response_time_of_get_method(environment, get_instance_booking_id):
    booking_id = get_instance_booking_id
    start = time.time()
    BookingAPI(environment).get_booking_by_id(booking_id)
    finish = time.time()
    assert finish - start <= 3.5


def test_change_ful_order_data(environment, create_booking):
    """ actual_data = BookingData(**optional data)
    response = BookingAPI(environment).change_full_data(BookingData(booking_number, actual_data.dict_to_json())
    expected_data= BookingData(**json.loads(response.text))"""
    actual_booking = create_booking
    response = BookingAPI(environment).get_booking_by_id(actual_booking.bookingid)
    booking_data = json.loads(response.text)
    expected_booking_data = BookingData.from_json(**booking_data)
    assert BookingData(**actual_booking.booking) == expected_booking_data


def test_change_some_attribute_order_data(environment, create_booking):
    """change_data = NewBookingData(**data)
    actual_data = BookingData(change_data.get_dict())
    response = BookingAPI(environment).change_full_data(BookingData(booking_number, actual_data.dict_to_json())
    expected_data= BookingData(**json.loads(response.text))"""
    actual_booking = create_booking
    response = BookingAPI(environment).get_booking_by_id(actual_booking.bookingid)
    booking_data = json.loads(response.text)
    expected_booking_data = BookingData.from_json(**booking_data)
    assert BookingData(**actual_booking.booking) == expected_booking_data


def test_delete_booking(environment, get_instance_booking_id):
    booking_id = get_instance_booking_id
    BookingAPI(environment).delete_booking(booking_id)
    get_all_bookings = BookingAPI(environment).get_all_bookings()
    bookings_list = sorted([number["bookingid"] for number in json.loads(get_all_bookings.text)])
    assert booking_id not in bookings_list


def test_delete_stauts_code(environment, get_instance_booking_id):
    booking_id = get_instance_booking_id
    response = BookingAPI(environment).delete_booking(booking_id)
    assert response.status_code == HTTPStatus.CREATED


def test_delete_exist_Booking_id(environment):
    get_all_bookings = BookingAPI(environment).get_all_bookings()
    bookings_list = sorted([number["bookingid"] for number in json.loads(get_all_bookings.text)])
    response = BookingAPI(environment).delete_booking(bookings_list[-1] + 2)
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
