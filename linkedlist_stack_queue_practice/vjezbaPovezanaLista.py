class Cvor:
    def __init__(self,element):
        self.element = element
        self.next = None

class PovezanaLista:
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
        while iteracija is not None:
            if iteracija.next.next is None:
                iteracija.next = None
            iteracija = iteracija.next

    def sortiraj(self):
        iteracija = self.glava
        while iteracija is not None:
            pomoc = iteracija.next
            while pomoc is not None:
                if pomoc.element < iteracija.element:
                    xvar = pomoc.element
                    pomoc.element = iteracija.element
                    iteracija.element = xvar
                pomoc = pomoc.next
            iteracija = iteracija.next

    def izbaciElementIndex(self,index):
        iteracija = self.glava
        brojac = 0
        while iteracija is not None:
            if index == 1:
                self.izbaciPocetak()
                break
            elif (brojac+1) == (index-1):
                iteracija.next = iteracija.next.next
            brojac += 1
            iteracija = iteracija.next

    def izbaciElementVrijednost(self,element):
        iteracija = self.glava
        while iteracija is not None:
            if iteracija.element == element:
                self.izbaciPocetak()
                break
            if iteracija.next.element == element and iteracija.next.next is not None:
                iteracija.next = iteracija.next.next
                break
            if iteracija.next.next is None and iteracija.next.element == element:
                iteracija.next = None
            iteracija = iteracija.next

    def pronadiIndexElementa(self,element):
        iteracija = self.glava
        brojac = 0
        while iteracija is not None:
            if iteracija.element == element:
                print("index elementa",element,"se nalazi na",brojac+1,"mjestu")
            brojac += 1
            iteracija = iteracija.next

    def pronadiElementNaIndexu(self,index):
        iteracija = self.glava
        brojac = 1
        while iteracija is not None:
            if brojac == index:
                print("na indexu",index,"se nalazi element",iteracija.element)
            brojac += 1
            iteracija = iteracija.next

    def velicina(self):
        iteracija = self.glava
        brojac = 0
        while iteracija is not None:
            brojac += 1
            iteracija = iteracija.next
        return brojac

    def prvaTri(self):
        lista = []
        iteracija = self.glava
        while iteracija is not None:
            if len(lista) >= 3:
                break
            else:
                lista.append(iteracija.element)
            iteracija = iteracija.next
        ntorka = tuple(lista)
        print("prva tri ili manje elementa ntorke su",ntorka)

    def zadnjaTri(self):
        iteracija = self.glava
        lista = []
        brojac = 0
        velicina = self.velicina()
        while iteracija is not None:
            if velicina-brojac <= 3:
                lista.append(iteracija.element)
            brojac += 1
            iteracija = iteracija.next
        ntorka = tuple(lista)
        print("zadnja tri ili manje elementa ntorke su",ntorka)

    def ubacivanjeNaIndex(self,element,index):
        brojac = 0
        self.dodajPocetak(element)
        iteracija = self.glava
        while iteracija is not None:
            if brojac == index-1:
                break
            else:
                pomoc = iteracija.next.element
                iteracija.next.element = iteracija.element
                iteracija.element = pomoc
            iteracija = iteracija.next
            brojac += 1

    def ubaciIza(self,prethodni,novi):
        self.dodajPocetak(novi)
        iteracija = self.glava
        while iteracija is not None:
            pomoc = iteracija.element
            iteracija.element = iteracija.next.element
            iteracija.next.element = pomoc
            if iteracija.element == prethodni:
                break
            iteracija = iteracija.next

    def izbaciKtiElement(self,k):
        iteracija = self.glava
        brojac = 0
        while iteracija.next is not None:
            if brojac == k-2 or k == 2:
                if iteracija.next.next is not None:
                    iteracija.next = iteracija.next.next
                    brojac = 0
                if iteracija.next.next is None and k == 2:
                    iteracija.next = None
                    break
            else:
                brojac += 1
            iteracija = iteracija.next


    def ispis(self):
        iteracija = self.glava
        while iteracija is not None:
            print(iteracija.element)
            iteracija = iteracija.next


if __name__ == '__main__':
    lista = PovezanaLista()
    lista.dodajPocetak(4)
    lista.dodajPocetak(78.3)
    lista.dodajPocetak(23.4)
    lista.dodajPocetak(101)
    lista.dodajPocetak(67)
    lista.dodajKraj(91)
    lista.dodajKraj(11.569)
    lista.dodajKraj(23.4)
    lista.dodajKraj(23.4)
    lista.dodajKraj(845)
    lista.dodajKraj(59)
    lista.dodajKraj(11)
    lista.izbaciPocetak()
    lista.izbaciKraj()
    lista.sortiraj()
    lista.izbaciElementIndex(4)
    lista.izbaciElementVrijednost(78.3)
    lista.ispis()
    lista.pronadiIndexElementa(23.4)
    lista.pronadiElementNaIndexu(6)
    velicina = lista.velicina()
    print("velicina liste je",velicina)
    lista.prvaTri()
    lista.zadnjaTri()
    lista.ubacivanjeNaIndex(0.003, 4)
    lista.ispis()
    print("---")
    lista.ubaciIza(59, 91.1)
    lista.ispis()
    print("---")
    lista.izbaciKtiElement(2)
    lista.ispis()