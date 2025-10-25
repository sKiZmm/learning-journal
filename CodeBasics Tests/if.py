def guess_number(num: int) -> str:
    if num == 42:
        return "You win!"
    return "Try again!"

print(guess_number(42)) # You win!
print(guess_number(61)) # Try again!