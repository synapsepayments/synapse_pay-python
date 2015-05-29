import synapsepay
import unittest

class TestAPIList(unittest.TestCase):
    def setUp(self):
        self.fake_resource = {"data" : "fake-data"}
        self.apilist = synapsepay.apibits.APIList(synapsepay.apibits.APIResource, [self.fake_resource])

    def test_setting_klass(self):
        self.assertEqual(synapsepay.apibits.APIResource, self.apilist.klass)

    def test_convert_data_to_klass_instances(self):
        self.assertIsInstance(self.apilist[0], synapsepay.apibits.APIResource)
        self.assertEqual(self.fake_resource, self.apilist[0].json)

