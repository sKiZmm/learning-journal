def count_chars(word: str, letter: str) -> int:
    i = 0
    count = 0

    while i < len(word):
        if word[i].lower() == letter.lower():
            count = count + 1
        i = i + 1
    return count

print(count_chars('HexlEt', 'e'))  # 2
print(count_chars('HexlEt', 'E'))  # 2