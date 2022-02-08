import json
import typing as t
import requests
from integration.exceptions import JPApiError


class ApiClient:

    EMPTY_RESPONSE_CODES = [204]

    def __init__(self, url):
        self.base_url = url

    def _get(self, endpoint, params: dict = None, headers: dict = None):
        return self._send('GET', endpoint, params=params, headers=headers)

    def _post(self, endpoint, data, params: dict = None, headers: dict = None):
        return self._send(
            'POST', endpoint, data=data, headers=headers, params=params
        )

    def _put(self, endpoint, data, params: dict = None, headers: dict = None):
        return self._send(
            'PUT', endpoint, data=data, params=params, headers=headers
        )

    def _patch(self, endpoint, data, params: dict = None, headers: dict = None):
        return self._send(
            'PATCH', endpoint, data=data, params=params, headers=headers
        )

    def _delete(self, endpoint, params: dict = None, headers: dict = None):
        return self._send(
            'DELETE', endpoint, params=params, headers=headers
        )

    def _send(
            self, method, endpoint, headers: dict = None,
            data: t.Union[t.List[t.Any], dict] = None, params: dict = None
    ):
        url = f"{self.base_url}/{endpoint}"
        request_kwargs = {
            "headers": {"Accept": "application/json; charset=UTF-8'"}
        }

        if headers is not None:
            request_kwargs['headers'].update(headers)

        if params is not None:
            request_kwargs['params'] = params

        if data is not None:
            request_kwargs['data'] = json.dumps(data, indent=2)

        try:
            response = requests.request(method, url, **request_kwargs)
            response.raise_for_status()
            if response.status_code in self.EMPTY_RESPONSE_CODES:
                return
            return response.json()
        except requests.RequestException as e:
            try:
                # Try to get the proper error message
                response = e.response
                message = e.response.text
                status_code = e.response.status_code
            except AttributeError:
                # If the exception has no response...
                response = None
                message = str(e)
                status_code = None
            raise JPApiError(message, status_code, response=response) from e
