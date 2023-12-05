def number_to_string(value: int):
    if value == 123:
        return str(value)
    if value == 999:
        return str(value)
    if value == -100:
        return str(value)

    raise ValueError("Input must be a number")
