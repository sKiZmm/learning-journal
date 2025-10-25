def normalize_url(url: str) -> str:
    if url[:8] == "https://":
        return url
    else:
        if url[:7] == "http://":
            url = f"https://{url[7:]}"
        else:
            url = f"https://{url}"
    return url


print(normalize_url('https://yahoo.com/'))  # => 'https://yahoo.com/'
print(normalize_url('google.com'))     # => 'https://google.com'
print(normalize_url('http://ai.fi'))   # => 'https://ai.fi'