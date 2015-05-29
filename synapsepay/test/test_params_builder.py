import synapsepay
import unittest

class TestParamsBuilder(unittest.TestCase):
    params = {
        'dog' : 'dog-value',
        'string' : 'string-value'
    }

    def setUp(self):
        self.alt_params = {
            'cat' : 'cat-value',
            'string' : 'alt-str-value'
        }
        self.merge_params = synapsepay.apibits.ParamsBuilder.merge(self.params, self.alt_params)

    def test_merge_all_values(self):
        self.assertEqual(self.merge_params['dog'], self.params['dog'])
        self.assertEqual(self.merge_params['cat'], self.alt_params['cat'])
        self.assertIsNotNone(self.merge_params['string'])

    def test_merge_priority(self):
        self.assertEqual(self.merge_params['string'], self.alt_params['string'])
