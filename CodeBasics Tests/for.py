def filter_string(string: str, char: str) -> str:
    filtered_string = ''

    for curr_char in string:
        if curr_char.lower() != char.lower():
            filtered_string = f"{filtered_string}{curr_char}"
    return filtered_string

text = 'If I look forward I win'
print(filter_string(text, 'i'))  # 'f  look forward  wn'
print(filter_string(text, 'O'))  # 'If I lk frward I win'