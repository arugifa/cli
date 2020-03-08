import re


def this_string(string: str, *, contains: str):
    pattern = re.sub(r'(\w+)', r'.*\1.*', contains)
    return re.match(pattern, string, flags=re.IGNORECASE)
