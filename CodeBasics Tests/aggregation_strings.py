def join_numbers_from_range(first: int, last: int) -> str:
    joined = ''
    i = first
    while i <= last:
        joined = joined + str(i)
        i = i + 1
    return joined

print(join_numbers_from_range(1, 1))   # '1'
print(join_numbers_from_range(2, 3))   # '23'
print(join_numbers_from_range(5, 10))  # '5678910'