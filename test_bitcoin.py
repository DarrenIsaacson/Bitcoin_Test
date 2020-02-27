import unittest
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin

class TestBitCoin(TestCase):

    @patch('bitcoin.get_json')
    def test_rate_value(self,mock_json):
        mock_rate = 555
        example_api_response = {'bpi':{'USD':{'rate_float':mock_rate}}}
        mock_json.side_effect = [example_api_response]
        converted = bitcoin.convert(10)

        self.assertEqual(5550 , converted)


    @patch('builtins.print')
    def test_display_total(self, mock_print):
        bitcoin.display(123)
        mock_print.assert_called_once_with('The rate of bitcoin is currently $123')





if __name__ == '__main__':
    unittest.main()
