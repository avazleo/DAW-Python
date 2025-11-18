class Animal:
    def hablar(self):
        return "...."

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

def main():
    animales = [Perro(), Gato(), Animal()]
    for a in animales:
        print(a.hablar())

if __name__ == "__main__":
    main()