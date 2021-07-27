class Cvor:
    def __init__(self,element):
        self.element = element
        self.next = None
        self.prev = None

class Red:
    def __init__(self):
        self.glava = None
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def stavi(self,element):
        cvor = Cvor(element)
        if self.isEmpty():
            self.glava = cvor
            self.size += 1
            return
        iteracija = self.glava
        while iteracija.next is not None:
            iteracija = iteracija.next
        iteracija.next = cvor
        cvor.next = None
        cvor.prev = iteracija
        self.rep = cvor
        self.size += 1

    def promijeni(self,element):
        iteracija = self.glava
        while iteracija is not None:
            if iteracija.element == element:
                if iteracija.next is not None or iteracija != self.glava:
                    iteracija.element = iteracija.prev.element * iteracija.next.element
            iteracija = iteracija.next

class Stog:
    def __init__(self):
        self.glava = None
        self.size = 0

    def stavi(self,element):
        cvor = Cvor(element)
        cvor.next = self.glava
        self.glava = cvor

    def uzmi(self):
        pomoc = self.glava.element
        self.glava = self.glava.next
        return pomoc

def ispisStoga(stog):
    iteracija = stog.glava
    while iteracija is not None:
        print(iteracija.element,end=",")
        iteracija = iteracija.next

if __name__ == '__main__':
    L = [1,2,3,4,5,6,7,8,9,10]
    S = Stog()
    R = Red()
    for element in L:
        R.stavi(element)

    S.stavi(5)
    S.stavi(5)
    S.stavi(22)
    S.stavi(14)
    S.stavi(6)
    S.stavi(9)

    ispisStoga(R)
    print()
    ispisStoga(S)

    R.promijeni(S.uzmi())
    R.promijeni(S.uzmi())
    R.promijeni(S.uzmi())
    R.promijeni(S.uzmi())
    R.promijeni(S.uzmi())

    print()
    print("------------")
    ispisStoga(R)
    print()
    ispisStoga(S)