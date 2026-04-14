import csv

FILE = "datos2.csv"

with open(FILE, 'at') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # delimiter es el carácter utilizado para separar cada campo. El valor predeterminado es la coma (',').
    # quotechar es el carácter utilizado para rodear los campos. El valor predeterminado es una comilla doble ('"').

    csv_writer.writerow(['Pepe López', 'Contable de la empresa', 'noviembre'])
    csv_writer.writerow(['Lola Flores', 'IT', 'enero'])