lenguajes = ["Python", "Java", "C++"]
f = open("lenguajes.txt", "wt")
for lenguaje in lenguajes:
    f.write(lenguaje + "\n")
f.close()

with open("lenguajes.txt", "wt") as f:
    for lenguaje in lenguajes:
        f.write(lenguaje + "\n")
