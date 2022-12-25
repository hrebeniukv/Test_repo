from api_framework.data.booking_data import BookingData
import json


class Booking:
    def __init__(self, **kwargs):
        self.bookingid = 9609 if "bookingid" not in kwargs else kwargs['bookingid']
        self.booking = BookingData().__dict__ if "booking" not in kwargs else BookingData(**kwargs['booking']).__dict__

    def dict_to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
