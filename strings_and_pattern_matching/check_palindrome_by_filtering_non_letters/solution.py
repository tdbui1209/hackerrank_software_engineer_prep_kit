def isAlphabeticPalindrome(code: str) -> bool:
    filterd_code = [i.lower() for i in code if i.isalpha()]
    return filterd_code == filterd_code[::-1]
