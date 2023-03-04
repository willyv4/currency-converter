import requests


def get_symbols():
    """
    Retrieves a list of currency symbols from the exchangerate.host API.

    Returns:
        A list of currency symbols (e.g. "USD", "EUR", "JPY").
    """

    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    symbol_data = response.json()

    symbol_lst = [symbol for symbol in symbol_data["symbols"]]

    return symbol_lst


def convert_currency(convert_from, convert_to, amount):
    """ 
    Converts a given amount of one currency to another currency using the exchangerate.host API.

    args: USD EUR 1500

    returns converstion for example € 4699.82
    """

    url = f'https://api.exchangerate.host/convert?from={convert_from}&to={convert_to}&amount={amount}&places=2'
    response = requests.get(url)
    data = response.json()
    rate_result = data["result"]

    return rate_result
