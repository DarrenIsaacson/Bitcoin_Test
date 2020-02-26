import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class TestBitCoin(TestCase):

    @patch('bitcoin.get_json')
    def test_rate_value(self,mock_json):
        mock_rate = 555
        example_api_response = {'bpi':{'USD':{'rate_float':mock_rate}}}
        mock_json.side_effect = [example_api_response]
        converted = bitcoin.convert(10)

        self.assertEqual(5550 , converted)

if __name__ == '__main__':
    unittest.main()
