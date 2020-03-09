import re


def this_string(string: str, *, contains: str):
    # Remove potential surrounding new lines,
    # to have a more beautiful regex at the end 💓
    pattern = contains.strip()

    # Surround individual words with .*
    pattern = re.sub(r'\s+', r'.*', pattern)

    # Surround text block to search with .*
    pattern = re.sub(r'^', r'.*', pattern)
    pattern = re.sub(r'$', r'.*', pattern)

    return bool(re.match(pattern, string, flags=re.IGNORECASE|re.DOTALL))


def this_exc(excinfo, *, contains: str):
    return this_string(str(excinfo), contains=contains)
