def print_reversed_word_by_symbol(word: str) -> None:
    i = len(word)
    while i > 0:
        print(word[i-1])
        i = i - 1

word = 'Hexlet'

print_reversed_word_by_symbol(word)