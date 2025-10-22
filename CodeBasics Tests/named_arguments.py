def trim_and_repeat(text, offset=0, repetitions=1):
    modified_text = f"{text[offset:] * repetitions}"
    return modified_text

text = "python"
print(trim_and_repeat(text, offset=3, repetitions=2)) # => honhon
print(trim_and_repeat(text, repetitions=3)) # => pythonpythonpython
print(trim_and_repeat(text)) # => python