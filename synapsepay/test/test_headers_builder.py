import synapsepay
import unittest

class TestHeadersBuilder(unittest.TestCase):
    headers = {
        'dog' : 'dog-value'
    }

    def setUp(self):
        self.built_headers = synapsepay.apibits.HeadersBuilder.build(self.headers)
        self.version = '0.0.2'

    def test_set_content_type(self):
        self.assertIn('Content-Type', self.built_headers)
        self.assertEqual('application/json', self.built_headers['Content-Type'])

    def test_set_user_agent(self):
        self.assertIn('User-Agent', self.built_headers)
        self.assertIn('Synapsepay', self.built_headers['User-Agent'])
        self.assertIn('0.0.6', self.built_headers['User-Agent'])

    # TODO: test_basic_auth_headers
