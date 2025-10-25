def filter_string(string: str, char: str) -> str:
    i = 0
    filtered_string = ''

    while i < len(string):
        if string[i] == char:
            filtered_string = filtered_string + ''
        else:
            filtered_string = filtered_string + string[i]
        i += 1
    return filtered_string

text = 'If I look back I am lost'
filter_string(text, 'I')  # 'f  look back  am lost'
filter_string(text, 'o')  # 'If I lk back I am lst'