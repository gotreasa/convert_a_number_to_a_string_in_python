def number_to_string(value: int):
    if not isinstance(value, int):
        raise ValueError("Input must be a number")
    return str(value)
