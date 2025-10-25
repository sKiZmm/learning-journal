def print_table_of_squares(lower: int, upper: int) -> None:
    for i in range(lower, upper + 1):
        print(f"square of {i} is {i**2}")

print_table_of_squares(1, 3)