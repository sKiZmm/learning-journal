def string_or_not(param) -> str:
    return isinstance(param, str) and 'yes' or 'no'

print(string_or_not('Hexlet')) # 'yes'
print(string_or_not(10)) # 'no'
print(string_or_not('') )# 'yes'
print(string_or_not(False)) # 'no'