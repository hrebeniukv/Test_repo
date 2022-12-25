import json


class NewBookingData:
    def __init__(self, **kwargs):
        if "firstname" in kwargs:
            self.firstname = kwargs['firstname']
        if "lastname" in kwargs:
            self.lastname = kwargs['lastname']
        if "totalprice" in kwargs:
            self.totalprice = kwargs['totalprice']
        if "depositpaid" in kwargs:
            self.depositpaid = kwargs['depositpaid']
        if "bookingdates" in kwargs:
            self.bookingdates = kwargs["bookingdates"]
        if "additionalneeds" in kwargs:
            self.additionalneeds = kwargs['additionalneeds']

    def get_dict(self):
        return self.__dict__

    def dict_to_json(self):
        return json.dumps(self.__dict__)


