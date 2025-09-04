import re

def is_valid_email(mail: str) -> bool:
    # Check for '@' symbol
    if '@' not in mail:
        return False
    # Check for at least one digit
    if not re.search(r'\d', mail):
        return False
    # Check for at least one special character (excluding '@')
    if not re.search(r'[!#$%^&*(),.?":{}|<>]', mail):
        return False
    return True
