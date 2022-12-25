import requests


class BaseAPI:
    def __init__(self, environment):
        self._base_url = environment.base_url
        self._headers = environment.headers
        self._request = requests

    def post(self, end_point, body, headers=None):
        if headers is None:
            headers = {"Content-Type": self._headers["Content-Type"]}
        response = self._request.post(f"{self._base_url}{end_point}", json=body, headers=headers)
        return response

    def get(self, end_point, booking_id=None, headers=None, ):
        if headers is None:
            headers = {"Content-Type": self._headers["Content-Type"]}
        if booking_id is None:
            response = self._request.get(f'{self._base_url}{end_point}', headers=headers)
        else:
            response = self._request.get(f'{self._base_url}{end_point}{booking_id}', headers=headers)
        return response

    def delete(self, end_point, booking_id, headers=None):
        if headers is None:
            headers = {"Content-Type": self._headers["Content-Type"], "Authorization": self._headers["Authorization"]}
        response = self._request.delete(f"{self._base_url}{end_point}{booking_id}", headers=headers)
        return response

    def patch(self, end_point, booking_id, new_data, headers=None):
        if headers is None:
            headers = {"Content-Type": self._headers["Content-Type"], "Accept": self._headers["Accept"],
                       "Cookie": self._headers["Cookie"]}
        return self._request.patch(f"{self._base_url}{end_point}{booking_id}", data=new_data, headers=headers)

    def put(self, end_point, booking_id, new_data, headers=None):
        if headers is None:
            headers = {"Content-Type": self._headers["Content-Type"], "Accept": self._headers["Accept"],
                       "Cookie": self._headers["Cookie"]}
        return self._request.put(f"{self._base_url}{end_point}{booking_id}", data=new_data, headers=headers)
