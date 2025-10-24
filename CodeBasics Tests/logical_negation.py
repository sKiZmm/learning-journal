def is_palindrome(text: str) -> bool:
    text = text.lower()
    return text == text[::-1]

def is_not_palindrome(text: str) -> bool:
    return not is_palindrome(text)