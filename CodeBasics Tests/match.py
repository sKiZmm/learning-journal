def get_number_explanation(num: int) -> str:
    match num:
        case 666:
            return "devil number"
        case 42:
            return "answer for everything"
        case 7:
            return "prime number"
        case _:
            return "just a number"
        
print(get_number_explanation(8))  # just a number
print(get_number_explanation(666))  # devil number
print(get_number_explanation(42))  # answer for everything
print(get_number_explanation(7))  # prime number