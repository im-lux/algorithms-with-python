class Cvor:
    def __init__(self,element):
        self.element = element
        self.next = None

class Lista:
    def __init__(self,lista=None):
        if lista is not None:
            self.glava = Cvor(lista[0])
            iteracija = self.glava
            for i in lista[1:]:
                iteracija.next = Cvor(i)
                iteracija = iteracija.next
        else:
            self.glava = None

    def makni(self):
        lista = []
        iteracija = self.glava
        brojac = 1
        while iteracija is not None:
            if brojac % 2 != 0:
                lista.append(iteracija.element)
            iteracija = iteracija.next
            brojac += 1
        self.glava = Cvor(lista[0])
        iteracija2 = self.glava
        for i in lista[1:]:
            iteracija2.next = Cvor(i)
            iteracija2 = iteracija2.next

def ispis(lista):
    lista.makni()
    iteracija = lista.glava
    while iteracija is not None:
        print(iteracija.element,end=",")
        iteracija = iteracija.next

def izdvoji(lista):
    druga = Lista()
    iteracija = lista.glava
    brojac = 1
    while iteracija is not None:
        if brojac % 2 == 0:
            tail = druga.glava
            if tail is None:
                cvor = Cvor(iteracija.element)
                cvor.next = druga.glava
                druga.glava = cvor
            else:
                while tail.next is not None:
                    tail = tail.next
                cvor = Cvor(iteracija.element)
                tail.next = cvor
                cvor.next = None
        iteracija = iteracija.next
        brojac += 1
    iteracija2 = druga.glava
    while iteracija2 is not None:
        print(iteracija2.element,end=",")
        iteracija2 = iteracija2.next
    print()

if __name__ == '__main__':
    L = Lista(['a','b','c','d','e','f','g','h'])
    izdvoji(L)
    ispis(L)