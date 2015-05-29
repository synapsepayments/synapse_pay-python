import synapsepay
import mock
import requests
import unittest

class TestAPIMethod(unittest.TestCase):
    method = "get"
    path = "/testing"
    params = { "param_a" : "1" }
    headers = { "header_a" : "a" }

    def setUp(self):
        self.object = synapsepay.apibits.APIResource()
        self.api_method = synapsepay.apibits.APIMethod(self.method, self.path, self.params, self.headers, self.object)

        self.client_id = 'test_id'
        self.client_secret = 'test_secret'
        self.api_base = 'http://test.apibits.com'

        synapsepay.CLIENT_ID = self.client_id
        synapsepay.CLIENT_SECRET = self.client_secret
        synapsepay.API_BASE = self.api_base

class TestAPIMethodInit(TestAPIMethod):

    def test_set_client_id(self):
        self.assertEqual(synapsepay.CLIENT_ID, self.client_id)

    def test_set_client_secret(self):
        self.assertEqual(synapsepay.CLIENT_SECRET, self.client_secret)

    def test_set_api_base(self):
        self.assertEqual(synapsepay.API_BASE, self.api_base)

    # @mock.patch('..apibits.requester.Requester.request', return_value=params)
    @mock.patch('synapsepay.apibits.path_builder.PathBuilder.build', return_value=TestAPIMethod.path)
    def test_pathbuilder_with_path_object_and_params(self, request_mock):
        apimethod = synapsepay.apibits.APIMethod(self.method, self.path, self.params, self.headers, self.object)
        request_mock.assert_called_once_with(self.object, self.params, self.path)

    @mock.patch('synapsepay.apibits.params_builder.ParamsBuilder.build', return_value=TestAPIMethod.params)
    def test_paramsbuilder_with_params(self, request_mock):
        apimethod = synapsepay.apibits.APIMethod(self.method, self.path, self.params, self.headers, self.object)
        request_mock.assert_called_once_with(self.params)

    @mock.patch('synapsepay.apibits.headers_builder.HeadersBuilder.build', return_value=TestAPIMethod.headers)
    def test_headersbuilder_with_params(self, request_mock):
        apimethod = synapsepay.apibits.APIMethod(self.method, self.path, self.params, self.headers, self.object)
        request_mock.assert_called_once_with(self.headers)

class TestAPIMethodExecute(TestAPIMethod):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.text = "{'status': 'success'}"
    mock_response.json = lambda: {'status': 'success'}

    mock_auth_error = mock.Mock()
    mock_auth_error.status_code = 401

    mock_invalid_json = "not-valid-json"

    @mock.patch('synapsepay.apibits.requester.Requester.request', side_effect=requests.Timeout())
    def test_api_error_on_failed_request(self, request_mock):
        with self.assertRaises(synapsepay.apibits.APIError):
            self.api_method.execute()

    @mock.patch('synapsepay.apibits.requester.Requester.request', return_value=mock_response)
    def test_response_parsed_as_json(self, request_mock):
        self.assertEqual({'status': 'success'}, self.api_method.execute())

    @mock.patch('synapsepay.apibits.requester.Requester.request', return_value=mock_auth_error)
    def test_401_status_authentication_error(self, request_mock):
        with self.assertRaises(synapsepay.apibits.AuthenticationError):
            self.api_method.execute()

    @mock.patch('requests.Response.content', mock_invalid_json)
    def test_invalid_json_api_error(self):
        with self.assertRaises(synapsepay.apibits.APIError):
            ret = self.api_method.execute()
