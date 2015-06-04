import synapsepay
import unittest

class TestPathBuilder(unittest.TestCase):
    class FakeResource(synapsepay.apibits.APIResource):
        _api_attributes = {'abc': ''}
        def __init__(self):
            super(TestPathBuilder.FakeResource, self).__init__({'abc': 'abc-value'})

    def setUp(self):
        self.params = {
            'dog' : 'dog-value',
        }
        self.object = TestPathBuilder.FakeResource()

    def test_object_attributes(self):
        path = "/a/:abc/123"
        expected = "/a/abc-value/123"

        actual = synapsepay.apibits.PathBuilder.build(self.object, None, path)
        self.assertEqual(expected, actual)

    def test_param_values(self):
        path = "/a/:dog/123"
        expected = "/a/dog-value/123"

        actual = synapsepay.apibits.PathBuilder.build(None, self.params, path)
        self.assertEqual(expected, actual)

    def test_attributes_and_params(self):
        path = "/a/:dog/:abc/123"
        expected = "/a/dog-value/abc-value/123"

        actual = synapsepay.apibits.PathBuilder.build(self.object, self.params, path)
        self.assertEqual(expected, actual)

    def test_missing_param(self):
        path = "/a/:dog/:abc/:cat/123"
        with self.assertRaises(ValueError):
            actual = synapsepay.apibits.PathBuilder.build(self.object, self.params, path)

