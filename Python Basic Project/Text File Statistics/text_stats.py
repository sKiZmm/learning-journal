text = open(r"Python Basic Project\Text File Statistics\text.txt", "rt")

def count_lines(file: object) -> int:
    count = 0
    file.seek(0)

    for lines in file:
        count += 1
    return count

def count_words(file: object) -> int:
    count = 0
    file.seek(0)

    for lines in file:
        lines = lines.split()
        count += len(lines)
    return count

def count_characters(file: object) -> int:
    count = 0
    file.seek(0)

    for lines in file:
        count += len(lines.rstrip("\n"))
    return count

def write_file(text: str) -> None:
    with open(r"Python Basic Project\Text File Statistics\text_summary.txt", "w+t") as f:
        f.write(text)
        f.seek(0)
        print(f.read())

def find_longest_word(file: object) -> str:
    longest_word = ''
    file.seek(0)

    for lines in file:
        lines = lines.split()
        for word in lines:
            if len(word) > len(longest_word):
                longest_word = word

    return longest_word
        
def find_average(file: object, total_words: int) -> float:
    file.seek(0)
    sum = 0

    for lines in file:
        lines = lines.split()
        for words in lines:
            sum += len(words)
    return sum / total_words

print(f"text.txt contains:\n{text.read()}\n")

lines = count_lines(text)
words = count_words(text)
characters = count_characters(text)
longest_word = find_longest_word(text)
average = find_average(text, words)
summary = f"text.txt has {lines} lines\ntext.txt has {words} words\ntext.txt has {characters} characters\ntext.txt longest word is {longest_word}\ntext.txt has an average word length of {average:.2f}"

write_file(summary)
print("\nFile output saved as text_summary.txt")

text.close()