from .errors import AuthenticationError, APIError, ConnectionError
from .headers_builder import HeadersBuilder
from .params_builder import ParamsBuilder
from .path_builder import PathBuilder
from .requester import Requester

import requests

class APIMethod(object):
    api_key = None
    api_base = None
    method = None
    path = None
    headers = {}
    params = {}

    def execute(self):
        try:
            response = Requester.request(self.method, self.url(), self.headers, self.params)
        except (requests.ConnectionError, requests.Timeout) as err:
            raise self.compose_error(err)

        if response.status_code == 401:
            text = response.text or "Authentication failed."
            raise AuthenticationError(text)
        elif response.status_code == 400:
            text = response.text or "Invalid request. Please check the URL and parameters."
            raise APIError(text)
        elif response.status_code == 404:
            text = response.text or "Invalid request. Please check the URL and parameters."
            raise APIError(text)
        elif response.status_code != 200:
            text = response.text or "An error occured while making the API call."
            raise APIError(text)

        try:
            return response.json()
        except ValueError:
            return APIError("Unable to parse the server response as JSON.")

    def compose_error(self, error):
        msg = "An error occurred while making the API call."

        if isinstance(error, requests.ConnectionError):
            msg = "An unexpected error occured while trying to connect to " \
            "the API. You may be seeing this message because your DNS is " \
            "not working. To check, try running from the command line."
        elif isinstance(error, requests.Timeout):
            msg = "The request timed out while making the API call."
        else:
            msg = "An unexpected error occured. If this problem persists let us know."

        return ConnectionError(msg)


    def url(self):
        return "%s%s" % (self.api_base, self.path)

    def __init__(self, method, path, params, headers, instance, api_key=None, api_base=None):
        from .. import API_BASE
        self.api_base = api_base or API_BASE
        self.method = method
        self.path = PathBuilder.build(instance, params, path)
        self.headers = HeadersBuilder.build(headers)
        self.params = ParamsBuilder.build(params)
