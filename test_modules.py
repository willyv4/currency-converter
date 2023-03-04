import re
import unittest
from unittest import result
from api_handles import get_symbols, convert_currency


class TestModules(unittest.TestCase):
    def test_get_symbols(self):

        result = get_symbols()
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 171)

    def test_convert_currency(self):

        result = [symbol for symbol in get_symbols()]

        new_result = [symbol for symbol in result if convert_currency(
            symbol, symbol, 1) is not None]

        for symbol in new_result:
            answer = convert_currency(symbol, symbol, 1)
            self.assertEqual(answer, 1)
