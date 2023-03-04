def handle_messages(convert_from, convert_to, amount, symbol_lst):
    """
    Checks if the user's input is valid and returns any error messages if not.

    Args:
        convert_from (str): The currency code to convert from.
        convert_to (str): The currency code to convert to.
        amount (float): The amount to convert.
        symbol_lst (list): A list of valid currency symbols.

    Returns:
        A list of error messages. Returns an empty list if there are no errors.
    """

    messages = []
    if convert_from not in symbol_lst:
        messages.append(f"Convert from: {convert_from} is an invalid currency")

    if convert_to not in symbol_lst:
        messages.append(f"Convert to: {convert_to} is an invalid currency")

    if amount == '':
        messages.append("Please enter an amount")

    if convert_from == convert_to:
        messages.append(
            "Convert from and convert to currencies cannot be the same")

    return messages
