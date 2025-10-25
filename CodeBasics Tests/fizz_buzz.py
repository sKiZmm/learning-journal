def fizzbuzz(num: int) -> str:
    result = ''
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            result += "FizzBuzz "
        elif i % 3 == 0:
            result += "Fizz "
        elif i % 5 == 0:
            result += "Buzz "
        else:
            result += f"{i} "
    return result.strip()

fizzbuzz(1) # => "1"
fizzbuzz(3) # => "1 2 Fizz"
fizzbuzz(5) # => "1 2 Fizz 4 Buzz"
fizzbuzz(15) # => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
