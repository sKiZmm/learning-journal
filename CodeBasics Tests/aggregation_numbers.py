def multiply_numbers_from_range(lower: int, upper: int) -> int:
    i = lower
    product = 1
    while i <= upper:
        product = product * i
        i = i + 1
    return product

print(multiply_numbers_from_range(1, 5))  # 1 * 2 * 3 * 4 * 5 = 120
print(multiply_numbers_from_range(2, 3))  # 2 * 3 = 6
print(multiply_numbers_from_range(6, 6))  # 6