import re

def password_check(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    # overall result
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )

    if password_ok == True:
        print("Passwort ist okay")
    else:
        print("Dein PW ist nicht sicher.")
        if length_error == True:
            print("Dein Passwort ist zu kurz")
        if digit_error == True:
            print("Dein Passwort enthält keine Zahlen")
        if uppercase_error == True:
            print("Dein Passwort enthält keine Großbuchstaben")
        if lowercase_error == True:
            print("Dein Passwort enthält keine Kleinbuchstaben")
        if symbol_error == True:
            print("Dein Passwort hat keine Sonderzeichen.")

"""     return {
        'password_ok' : password_ok,
        'length_error' : length_error,
        'digit_error' : digit_error,
        'uppercase_error' : uppercase_error,
        'lowercase_error' : lowercase_error,
        'symbol_error' : symbol_error,
    }
 """

    
password_check("abc")