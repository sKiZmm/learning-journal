def is_international_phone(number: str) -> bool:
    first_char = number[0]
    return first_char == '+'

print(is_international_phone('89602223423'))  # False
print(is_international_phone('+79602223423')) # True