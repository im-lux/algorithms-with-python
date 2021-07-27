class Cvor:
    def __init__(self,element):
        self.element = element
        self.next = None
        self.prev = None

class Red:
    def __init__(self):
        self.glava = None
        self.rep = None
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def enqueue(self,element):
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

    def dequeue(self):
        element = self.glava.element
        self.glava = self.glava.next
        self.size -= 1
        print("skinut je element",element)

    def first(self):
        print("prvi element",self.glava.element)

    def velicina(self):
        vel = self.size
        print("veličina reda je",vel)

    def printqueue(self):
        iteracija = self.glava
        while iteracija is not None:
            print(iteracija.element)
            iteracija = iteracija.next

if __name__ == '__main__':
    red = Red()
    print(red.isEmpty())
    red.enqueue(3)
    red.enqueue(88.9)
    red.enqueue(11.3)
    red.enqueue(44.4)
    red.enqueue(2.9)
    red.printqueue()
    red.dequeue()
    print("ispis nakon skidanja prvog:")
    red.printqueue()
    red.first()
    red.velicina()
    print(red.isEmpty())