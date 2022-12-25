import json


class BookingData:
    def __init__(self, **kwargs):
        self.firstname = 'John' if "firstname" not in kwargs else kwargs['firstname']
        self.lastname = 'Allen' if "lastname" not in kwargs else kwargs['lastname']
        self.totalprice = 111 if "totalprice" not in kwargs else kwargs['totalprice']
        self.depositpaid = True if "depositpaid" not in kwargs else kwargs['depositpaid']
        self.bookingdates = {'checkin': '2018-01-01', 'checkout': '2019-01-01'} if "bookingdates" not in kwargs else \
        kwargs["bookingdates"]
        self.additionalneeds = 'superb owls' if "additionalneeds" not in kwargs else kwargs['additionalneeds']

    def dict_to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

