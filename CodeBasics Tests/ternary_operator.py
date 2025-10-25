def flip_flop(word: str) -> str:
    return "flop" if word == "flip" else "flip"

print(flip_flop('flip'))  # => 'flop'
print(flip_flop('flop'))  # => 'flip'