import re

def validar_password(p):
    patron = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^\w\s])[^\s]{8,}$"
    return bool(re.match(patron, p))

print(validar_password("1Aa%&jueie"))