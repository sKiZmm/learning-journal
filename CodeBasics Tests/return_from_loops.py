def is_contains_char(line: str, letter: str) -> bool:
    i = 0

    while i < len(line):
        if line[i] == letter:
            return True
        i += 1
    return False

print(is_contains_char('Hexlet', 'H'))  # => True
print(is_contains_char('Hexlet', 'h'))  # => False
print(is_contains_char('Awesomeness', 'm'))  # => True
print(is_contains_char('Awesomeness', 'd'))  # => False