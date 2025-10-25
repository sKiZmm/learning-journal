def print_reversed_numbers(num: int) -> None:
    i = num

    while i >= 1:
        print(i)
        i = i - 1
    print("finished!")

print_reversed_numbers(4)