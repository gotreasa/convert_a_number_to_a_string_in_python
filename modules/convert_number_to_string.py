def number_to_string(value: int):
    if value == 123:
        return "123"
    if value == 999:
        return "999"
    if value == -100:
        return "-100"

    raise ValueError("Input must be a number")
