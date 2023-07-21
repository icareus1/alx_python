def validate_password(password):
    length = len(password) >= 8
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    digit = any(char.isdigit() for char in password)
    space = ' ' not in password
    
    return length and uppercase and lowercase and digit and space