import re

dni = "12345678Z"
print(re.sub(r"(\d{6})(\d{2}[A-Z])", r"******\2", dni))