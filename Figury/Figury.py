
from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def nazwa(self):
        pass

    def wypisz(self):
        print(f"Jestem {self.nazwa()}. Moj obwod: {self.obwod()}, a pole: {self.pole()}.")

    @abstractmethod
    def obwod(self):
        pass

    @abstractmethod
    def pole(self):
        pass
class Trojkat(Figura):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def nazwa(self):
        return "Trójkąt"

    def obwod(self):
        return self.a + self.b + self.c

    def pole(self):
        p = self.obwod()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

class Kolo(Figura):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def nazwa(self):
        return "Koło"

    def obwod(self):
        return 2 * math.pi * self.r

    def pole(self):
        return math.pi * self.r ** 2

class Kwadrat(Figura):
    def __init__(self, a):
        self.a = a

    def nazwa(self):
        return "Kwadrat"

    def obwod(self):
        return 4 * self.a

    def pole(self):
        return self.a ** 2

class Prostokat(Kwadrat):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def nazwa(self):
        return "Prostokąt"

    def obwod(self):
        return 2 * (self.a + self.b)

    def pole(self):
        return self.a * self.b

def main():
    t = Trojkat(3.0, 4.0, 5.0)
    t.wypisz()
    k = Kolo(4, 5, 1)
    k.wypisz()
    kw = Kwadrat(3)
    kw.wypisz()
    p = Prostokat(4, 5)
    p.wypisz()

    lista_figur = [t, k, kw, p]
    suma_pol = 0
    suma_obwodow = 0
    for f in lista_figur:
        suma_pol += f.pole()
        suma_obwodow += f.obwod()

    print(f"Suma pol wynosi: ", suma_pol)
    print(f"Suma obwodow wynosi: ", suma_obwodow)

if __name__ == "__main__":
    main()