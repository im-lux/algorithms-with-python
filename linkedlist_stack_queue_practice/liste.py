#---------------------------------------------------------
#JEDNOSTRUKA LISTA
# class Cvor:
#     def __init__(self, element):
#         self.element = element
#         self.next = None
#
#     def getElement(self):
#         return self.element
#
#     def getNext(self):
#         return self.next
#
#     def setElement(self, element):
#         self.element = element
#
#     def setNext(self, next):
#         self.next = next
#
# class VezanaLista:
#     def __init__(self):
#         self.glava = None
#         self.rep = None
#
#     def dodajPocetak(self, element):
#         cvor = Cvor(element)
#         cvor.next = self.glava
#         self.glava = cvor
#
#     def dodajKraj(self, element):
#         cvor = Cvor(element)
#         zadnja = self.glava
#         while (zadnja.next):
#             zadnja = zadnja.next
#         zadnja.next = cvor
#
#     def izbaciPocetak(self):
#         self.glava = self.glava.next
#
#     def izbaciOdredeniElement(self, element):
#         trenutni = self.glava
#         prethodni = None
#         naden = False
#         while not naden:
#             if trenutni.getElement() == element:
#                 naden = True
#             else:
#                 prethodni = trenutni
#                 trenutni = trenutni.getNext()
#         if prethodni == None:
#             self.glava = trenutni.getNext()
#         else:
#             prethodni.setNext(trenutni.getNext())
#
#     def micanjeDuplikata(self):
#         pomoc = self.glava
#         while pomoc.next is not None:
#             if pomoc.element == pomoc.next.element:
#                 novi = pomoc.next.next
#                 pomoc.next = None
#                 pomoc.next = novi
#             else:
#                 pomoc = pomoc.next
#         return self.glava
#
#     def ispis(self):
#         cvor = self.glava
#         while cvor:
#             print(cvor.getElement())
#             cvor = cvor.getNext()
#
# if __name__ == '__main__':
#     lista = VezanaLista()
#     lista.dodajPocetak(5)
#     lista.dodajPocetak(2.7)
#     lista.dodajPocetak(3.3)
#     lista.dodajKraj(4)
#     lista.dodajKraj(5)
#     lista.dodajKraj(89.3)
#     lista.dodajKraj(5)
#     lista.izbaciPocetak()
#     lista.izbaciOdredeniElement(4)
#     lista.micanjeDuplikata()
#     lista.ispis()

#---------------------------------------------------------
# class Cvor:
#     def __init__(self,element):
#         self.element = element
#         self.next = None
#
# class VezanaLista(Cvor):
#     def __init__(self):
#         self.glava = None
#
#     def dodajPocetak(self,element):
#         cvor = Cvor(element)
#         cvor.next = self.glava
#         self.glava = cvor
#
#     def dodajKraj(self,element):
#         cvor = Cvor(element)
#         iteracija = self.glava
#         while iteracija.next is not None:
#             iteracija = iteracija.next
#         iteracija.next = cvor
#         cvor.next = None
#
#     def izbaciPocetak(self):
#         self.glava = self.glava.next
#
#     def izbaciKraj(self):
#         iteracija = self.glava
#         while iteracija.next.next is not None:
#             iteracija = iteracija.next
#         iteracija.next = None
#
#     def sortiraj(self):
#         iteracija = self.glava
#         pomoc = None
#         while iteracija is not None:
#             pomoc = iteracija.next
#             while pomoc is not None:
#                 if iteracija.element > pomoc.element:
#                     cvor = iteracija.element
#                     iteracija.element = pomoc.element
#                     pomoc.element = cvor
#                 pomoc = pomoc.next
#             iteracija = iteracija.next
#
#     def izbaciElementIndex(self,index):
#         iteracija = self.glava
#         brojac = 1
#         while iteracija is not None:
#             if brojac == index:
#                 cvor = iteracija.next.next
#                 iteracija.next = cvor
#             brojac += 1
#             iteracija = iteracija.next
#
#     def izbaciElementVrijednost(self,vrijednost):
#         iteracija = self.glava
#         while iteracija.next is not None:
#             if iteracija.next.element == vrijednost:
#                 cvor = iteracija.next.next
#                 iteracija.next = cvor
#             iteracija = iteracija.next
#
#     def pronadiIndexElementa(self,element):
#         index = 0
#         iteracija = self.glava
#         while iteracija is not None:
#             if iteracija.element == element:
#                 break
#             index += 1
#             iteracija = iteracija.next
#         print("element", element, "se nalazi na indexu",index+1,"( ako gledamo programerski onda je to index",index,")")
#
#     def pronadiElementNaIndexu(self,index):
#         element = 0
#         brojac = 1
#         iteracija = self.glava
#         while iteracija is not None:
#             if brojac == index:
#                 element = iteracija.element
#                 break
#             brojac += 1
#             iteracija = iteracija.next
#         print("na indexu",index,"se nalazi element",element,"( programerski gledano radi se o indexu",index-1,")")
#
#     def ubacivanjeNaIndex(self,element,index):
#         cvor = Cvor(element)
#         cvor.next = self.glava
#         self.glava = cvor
#         iteracija = self.glava
#         brojac = 1
#         while iteracija is not None:
#             if brojac != index:
#                 pomoc = iteracija.element
#                 iteracija.element = iteracija.next.element
#                 iteracija.next.element = pomoc
#             else:
#                 break
#             brojac += 1
#             iteracija = iteracija.next
#
#     def izbaciDuplikata(self):
#         iteracija = self.glava
#         while iteracija is not None:
#             pomoc = iteracija.next
#             while pomoc is not None:
#                 if pomoc.element == iteracija.element:
#                     trenutni = self.glava
#                     while (trenutni and trenutni.next != pomoc):
#                         trenutni = trenutni.next
#                     trenutni.next = pomoc.next
#                 pomoc = pomoc.next
#             iteracija = iteracija.next
#
#     def izbrisiSve(self):
#         self.glava = None
#
#     def ispis(self):
#         cvor = self.glava
#         while cvor:
#             print(cvor.element)
#             cvor = cvor.next
#
#
# if __name__ == '__main__':
#     lista = VezanaLista()
#     lista.dodajPocetak(3)
#     lista.dodajPocetak(5.8)
#     lista.dodajPocetak(77.13)
#     lista.dodajKraj(678)
#     lista.dodajKraj(678)
#     lista.dodajKraj(5.8)
#     lista.dodajPocetak(77.7)
#     lista.dodajPocetak(43)
#     lista.dodajPocetak(5.8)
#     lista.izbaciPocetak()
#     lista.izbaciKraj()
#     lista.sortiraj()
#     lista.izbaciElementIndex(1)
#     lista.izbaciElementVrijednost(43)
#     # lista.izbrisiSve()
#     lista.ispis()
#     lista.pronadiIndexElementa(77.7)
#     lista.pronadiElementNaIndexu(3)
#     print("\n")
#     lista.ubacivanjeNaIndex(44.44, 4)
#     lista.izbaciDuplikata()
#     lista.ispis()


#-----------------------------------------------------------------------
#DVOSTRUKO POVEZANA LISTA
# class Cvor:
#     def __init__(self,element):
#         self.next = None
#         self.prev = None
#         self.element = element
#
# class DvostrukoVezanaLista(Cvor):
#     def __init__(self):
#         self.glava = None
#         self.tail = None
#
#     def dodajPocetak(self,element):
#         cvor = Cvor(element)
#         cvor.next = self.glava
#         self.glava = cvor
#
#     def dodajKraj(self,element):
#         cvor = Cvor(element)
#         iteracija = self.glava
#         while iteracija.next is not None:
#             iteracija = iteracija.next
#         iteracija.next = cvor
#         cvor.next = None
#         cvor.prev = iteracija
#
#     def ispis(self):
#         iteracija = self.glava
#         while iteracija is not None:
#             print(iteracija.element)
#             iteracija = iteracija.next
#
#     def obrni(self):
#         iteracija = self.glava
#         pomoc = None
#         while iteracija is not None:
#             pomoc = iteracija.prev
#             iteracija.prev = iteracija.next
#             iteracija.next = pomoc
#             iteracija = iteracija.prev
#         if pomoc is not None:
#             self.glava = pomoc.prev
#
# if __name__ == '__main__':
#     lista = DvostrukoVezanaLista()
#     lista.dodajPocetak(3)
#     lista.dodajPocetak(77.54)
#     lista.dodajPocetak(11.2)
#     lista.dodajKraj(8)
#     lista.dodajKraj(9.99)
#     lista.dodajKraj(23)
#     lista.ispis()
#     print()
#     lista.obrni()
#     lista.ispis()


#STOG
# class Cvor:
#     def __init__(self,element,next):
#         self.element = element
#         self.next = next
#
# class PovezaniStog(Cvor):
#     def __init__(self):
#         self.glava = None
#         self.size = 0
#
#     def velicina(self):
#         return self.size
#
#     def dodaj(self,element):
#         cvor = Cvor(element,self.glava)
#         self.glava = cvor
#         self.size += 1
#
#     def vratiTop(self):
#         return self.glava.element
#
#     def makni(self):
#         cvor = self.glava.next
#         self.glava = cvor
#         self.size -= 1
#
#     def ispis(self):
#         iteracija = self.glava
#         while iteracija is not None:
#             print(iteracija.element)
#             iteracija = iteracija.next
#
#
# if __name__ == '__main__':
#     stog = PovezaniStog()
#     stog.dodaj(2)
#     stog.dodaj(5.77)
#     stog.dodaj(0.1)
#     stog.ispis()
#     print("na vrhu je",stog.vratiTop())
#     print("novi ispis:")
#     stog.makni()
#     stog.ispis()
#     print("velicina: ",stog.velicina())


#CIRKULARNI RED
# class CirkularniRed:
#     def __init__(self,velicina):
#         self.red = list()
#         self.maxVelicina = velicina
#         self.glava = 0
#         self.rep = 0
#
#     def dodaj(self,element):
#         if self.size() == self.maxVelicina-1:
#             return "red je pun!"
#         else:
#             self.red.append(element)
#             self.rep = (self.rep+1) % self.maxVelicina
#
#     def makni(self):
#         element = self.red[self.glava]
#         self.glava = (self.glava+1) % self.maxVelicina
#
#     def size(self):
#         velicina = self.rep - self.glava
#
# if __name__ == '__main__':
#     red = CirkularniRed(5)
#     red.dodaj(3)
#     red.dodaj(7)
#     red.dodaj(13.45)
#     red.dodaj(99.13)

#RED
class Cvor:
    def __init__(self,element):
        self.element = element
        self.next = None

class Red(Cvor):
    def __init__(self):
        self.glava = None
        self.tail = None
        self.size = 0

    def velicina(self):
        return self.size

    def prvi(self):
        return self.glava.element

    def dodaj(self,element):
        cvor = Cvor(element)
        if self.size == 0:
            self.glava = cvor
        else:
            self.tail.next = cvor
        self.tail = cvor
        self.size += 1

    def makni(self):
        cvor = self.glava.next
        self.glava = cvor
        self.size -= 1

    def ispis(self):
        iteracija = self.glava
        while iteracija is not None:
            print(iteracija.element)
            iteracija = iteracija.next

if __name__ == '__main__':
    red = Red()
    red.dodaj(3)
    red.dodaj(77.87)
    red.dodaj('jao')
    red.ispis()
    print("prvi element je", red.prvi())
    print("velicina reda je",red.velicina())
    red.makni()
    red.ispis()


