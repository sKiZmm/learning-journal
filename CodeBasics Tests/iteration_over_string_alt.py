def add_spaces(word: str) -> None:
    i = 1
    spaced_word = word[0]
    while i < len(word):
        spaced_word = f"{spaced_word} {word[i]}"
        i = i + 1
    return spaced_word

print(add_spaces("hex"))
print(add_spaces("Arya"))