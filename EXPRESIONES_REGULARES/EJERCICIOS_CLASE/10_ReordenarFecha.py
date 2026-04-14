import re

fecha = "12/03/2026"
print(re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", fecha))