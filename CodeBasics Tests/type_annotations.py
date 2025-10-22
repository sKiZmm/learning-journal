def word_multiply(word: str, repetition: int=1) -> str:
    return word * repetition

text = 'python'
print(word_multiply(text, 2)) # => pythonpython
print(word_multiply(text, 0)) # =>