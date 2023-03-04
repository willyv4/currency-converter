import requests


def get_symbols():
    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    symbol_data = response.json()

    symbol_lst = []
    for symbols in symbol_data["symbols"]:
        symbol_lst.append(symbols)

    return symbol_lst


def convert_currency(convert_from, convert_to, amount):
    url = f'https://api.exchangerate.host/convert?from={convert_from}&to={convert_to}&amount={amount}&places=2'
    response = requests.get(url)
    data = response.json()
    rate_result = data["result"]
    return rate_result
