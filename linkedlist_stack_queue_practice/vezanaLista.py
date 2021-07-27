class Cvor:
    def __init__(self,element):
        self.glava = None
        self.element = element

class VezanaLista(Cvor):
    def __init__(self):
        self.glava = None

    def dodajPocetak(self,element):
        cvor = Cvor(element)
        cvor.next = self.glava
        self.glava = cvor

    def dodajKraj(self,element):
        cvor = Cvor(element)
        iteracija = self.glava
        while iteracija is not None:
            if iteracija.next is None:
                iteracija.next = cvor
                cvor.next = None
            iteracija = iteracija.next

    def izbaciPocetak(self):
        self.glava = self.glava.next

    def izbaciKraj(self):
        iteracija = self.glava
        while iteracija.next.next is not None:
            iteracija = iteracija.next
        iteracija.next = None

    def sortiraj(self):
        iteracija = self.glava
        while iteracija is not None:
            if iteracija.next is None:
                break
            else:
                pomoc = iteracija.next
                while pomoc is not None:
                    if iteracija.element < pomoc.element:
                        priv = iteracija.element
                        iteracija.element = pomoc.element
                        pomoc.element = priv
                    pomoc = pomoc.next
            iteracija = iteracija.next

    def izbaciElementIndex(self,index):
        iteracija = self.glava
        brojac = 1
        while iteracija:
            if brojac == (index-1):
                pomoc = iteracija.next.next
                iteracija.next = pomoc
                break
            else:
                brojac += 1
            iteracija = iteracija.next

    def izbaciElementVrijednost(self,element):
        iteracija = self.glava
        while iteracija:
            if iteracija.next == None and iteracija.element != element:
                print("nema takvog elementa")
                break
            if self.glava.element == element:
                self.glava = self.glava.next
                break
            if iteracija.next.element == element:
                iteracija.next = iteracija.next.next
                break
            iteracija = iteracija.next

    def pronadiIndexElementa(self,element):
        index = 0
        iteracija = self.glava
        while iteracija is not None:
            if iteracija.element == element:
                break
            index += 1
            iteracija = iteracija.next
        print("element", element, "se nalazi na indexu",index+1,"( ako gledamo programerski onda je to index",index,")")

    def pronadiElementNaIndexu(self,index):
        element = 0
        brojac = 1
        iteracija = self.glava
        while iteracija is not None:
            if brojac == index:
                element = iteracija.element
                break
            brojac += 1
            iteracija = iteracija.next
        print("na indexu",index,"se nalazi element",element,"( programerski gledano radi se o indexu",index-1,")")

    def velicina(self):
        brojac = 0
        iteracija = self.glava
        while iteracija is not None:
            brojac += 1
            iteracija = iteracija.next
        return brojac

    def prvaTri(self):
        lista = []
        iteracija = self.glava
        while iteracija is not None:
            if len(lista)+1 > 3:
                break
            else:
                lista.append(iteracija.element)
            iteracija = iteracija.next
        ntorka = tuple(lista)
        return ntorka

    def zadnjaTri(self):
        lista = []
        iteracija = self.glava
        vel = self.velicina()
        brojac = 0
        while iteracija is not None:
            if (vel - brojac) <= 3:
                lista.append(iteracija.element)
            else:
                brojac += 1
            iteracija = iteracija.next
        ntorka = tuple(lista)
        return ntorka

    def ubacivanjeNaIndex(self,element,index):
        cvor = Cvor(element)
        cvor.next = self.glava
        self.glava = cvor
        iteracija = self.glava
        brojac = 1
        while iteracija is not None:
            if brojac != index:
                pomoc = iteracija.element
                iteracija.element = iteracija.next.element
                iteracija.next.element = pomoc
            else:
                break
            brojac += 1
            iteracija = iteracija.next

    def ubaciIza(self,prethodni,element):
        cvor = Cvor(element)
        iteracija = self.glava
        while iteracija is not None:
            if iteracija.element == prethodni:
                cvor.next = iteracija.next
                iteracija.next = cvor
            iteracija = iteracija.next

    def izbaciDuplikata(self):
        iteracija = self.glava
        while iteracija is not None:
            if iteracija.next is None:
                break
            else:
                pomoc = iteracija.next
                while pomoc is not None:
                    if iteracija.element == pomoc.element:
                        trenutni = self.glava
                        while (trenutni and trenutni.next != pomoc):
                            trenutni = trenutni.next
                        trenutni.next = pomoc.next
                    pomoc = pomoc.next
            iteracija = iteracija.next

    def ispis(self):
        iteracija = self.glava
        while iteracija is not None:
            print(iteracija.element)
            iteracija = iteracija.next

if __name__ == '__main__':
    lista = VezanaLista()
    lista.dodajPocetak(3.6)
    lista.dodajPocetak(1.89)
    lista.dodajPocetak(83)
    lista.dodajPocetak(4.44)
    lista.dodajPocetak(9.1)
    lista.dodajKraj(44.1)
    lista.dodajKraj(31)
    lista.dodajKraj(77.3)
    lista.izbaciPocetak()
    lista.izbaciKraj()
    lista.ispis()
    print("ispis nakon sorta")
    lista.sortiraj()
    lista.izbaciElementIndex(2)
    lista.izbaciElementVrijednost(4.44)
    lista.ispis()
    size = lista.velicina()
    print("velicina",size)
    ntorka = lista.prvaTri()
    print(ntorka)
    ntorka2 = lista.zadnjaTri()
    print(ntorka2)
    lista.ubaciIza(83,98)
    lista.dodajPocetak(1)
    lista.dodajKraj(78.3)
    lista.dodajPocetak(98)
    lista.dodajKraj(98)
    lista.izbaciDuplikata()
    lista.ubacivanjeNaIndex(100,2)
    lista.ubaciIza(3.6,0.003)
    lista.ispis()
