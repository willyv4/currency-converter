from app import app
import unittest
from handle_messages import handle_messages
from app import app

app.config['SECRET_KEY'] = "IAMCOOL1234"


class TestModules(unittest.TestCase):
    def test_handle_messages_valid_currencies(self):
        symbol_lst = ['USD', 'EUR', 'GBP', 'JPY']
        messages = handle_messages('USD', 'EUR', '10', symbol_lst)
        self.assertEqual(messages, [])

    def test_handle_messages_invalid_convert_from_currency(self):
        symbol_lst = ['USD', 'EUR', 'GBP', 'JPY']
        messages = handle_messages('XXX', 'EUR', '10', symbol_lst)
        self.assertEqual(
            messages, ["Convert from: XXX is an invalid currency"])

    def test_handle_messages_invalid_convert_to_currency(self):
        symbol_lst = ['USD', 'EUR', 'GBP', 'JPY']
        messages = handle_messages('USD', 'XXX', '10', symbol_lst)
        self.assertEqual(messages, ["Convert to: XXX is an invalid currency"])

    def test_handle_messages_empty_amount(self):
        symbol_lst = ['USD', 'EUR', 'GBP', 'JPY']
        messages = handle_messages('USD', 'EUR', '', symbol_lst)
        self.assertEqual(messages, ["Please enter an amount"])

    def test_handle_messages_same_convert_from_and_to_currencies(self):
        symbol_lst = ['USD', 'EUR', 'GBP', 'JPY']
        messages = handle_messages('USD', 'USD', '10', symbol_lst)
        self.assertEqual(
            messages, ["Convert from and convert to currencies cannot be the same"])


class TestApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def test_convert_route(self):
        response = self.app.post(
            "/",
            data=dict(
                convert_from="USD",
                convert_to="EUR",
                amount="100"
            ),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_rate_response_route(self):
        with self.app.session_transaction() as session:
            session["convert_from"] = "USD"
            session["convert_to"] = "EUR"
            session["amount"] = "100"

        response = self.app.get("/rate-response")
        self.assertEqual(response.status_code, 200)
