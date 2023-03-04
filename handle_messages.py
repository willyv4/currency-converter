def handle_messages(convert_from, convert_to, amount, symbol_lst):
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
