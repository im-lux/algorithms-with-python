class Cvor:
    def __init__(self,element):
        self.element = element
        self.next = None
        self.prev = None

class Lista:
    def __init__(self,lista=None):
        if lista is not None:
            self.glava = Cvor(lista[0])
            iteracija = self.glava
            iteracija.prev = None
            for i in lista[1:]:
                iteracija.next = Cvor(i)
                iteracija.next.prev = iteracija
                iteracija = iteracija.next
        else:
            self.glava = None

    def ispis(self):
        iteracija = self.glava
        while iteracija is not None:
            print(iteracija.element,end=",")
            iteracija = iteracija.next

def izdvoji(lista):
    pomoc = []
    iteracija = lista.glava
    while iteracija is not None:
        if isinstance(iteracija.element, int):
            pomoc.append(iteracija.element)
        iteracija = iteracija.next
    druga = Lista(pomoc)
    xvar = druga.glava
    while xvar.next is not None:
        xvar = xvar.next
    while xvar is not None:
        print(xvar.element,end=",")
        xvar = xvar.prev

def izdvoji2(lista):
    pomoc = []
    iteracija = lista.glava
    while iteracija is not None:
        if isinstance(iteracija.element, str):
            pomoc.append(iteracija.element)
        iteracija = iteracija.next
    lista = Lista(pomoc)
    xvar = lista.glava
    while xvar.next is not None:
        xvar = xvar.next
    while xvar is not None:
        print(xvar.element,end=",")
        xvar = xvar.prev


if __name__ == '__main__':
    L = Lista([33, "asp", "oop1", 5, 21, "python", 2, "c++"])
    L.ispis()
    print()
    izdvoji(L)
    print()
    izdvoji2(L)