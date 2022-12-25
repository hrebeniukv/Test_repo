from api_framework.data.booking import Booking
from api_framework.data.booking_data import BookingData
from api_framework.data.new_booking_data import NewBookingData

from api_framework.utilites.base_api import BaseAPI



class BookingAPI(BaseAPI):
    def __init__(self, environment):
        super().__init__(environment)
        self.__booking_url = "booking/"

    def get_booking_by_id(self, booking_id):
        return self.get(self.__booking_url, booking_id)

    def get_all_bookings(self):
        return self.get(self.__booking_url)

    def create_new_booking(self):
        booking_data = Booking()
        body_json = booking_data.dict_to_json()
        return self.post(self.__booking_url, body_json)

    def delete_booking(self, booking_id):
        return self.delete(self.__booking_url, booking_id)

    def change_booking_attribute(self, booking_id, new_data):
        new_booking_data = NewBookingData(**new_data)
        body_json = new_booking_data.dict_to_json()
        return self.patch(self.__booking_url, booking_id, new_data=body_json)

    def change_full_data(self, booking_id, new_data=None):
        if new_data is None:
            new_booking_data = BookingData()
        else:
            new_booking_data = BookingData(**new_data)
        body_json = new_booking_data.dict_to_json()
        return self.put(self.__booking_url, booking_id, new_data=body_json)

