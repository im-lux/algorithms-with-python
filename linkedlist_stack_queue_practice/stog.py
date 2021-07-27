class Cvor:
    def __init__(self,element):
        self.element = element
        self.next = None
        self.prev = None

class Stog:
    def __init__(self):
        self.glava = None
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self,element):
        cvor = Cvor(element)
        if self.isEmpty():
            cvor.next = None
            cvor.prev = None
            self.glava = cvor
            self.size += 1
        else:
            cvor.next = self.glava
            cvor.prev = None
            self.glava = cvor
            self.size += 1

    def pop(self):
        if self.isEmpty():
            print("Stog je prazan")
            return
        else:
            self.glava = self.glava.next
            self.size -= 1

    def top(self):
        if self.isEmpty():
            print("NEMA TOPA,PRAZAN STOG")
            return
        else:
            print("top element:",self.glava.element)

    def velicina(self):
        print("veličina stoga:",self.size)

    def ispis(self):
        iteracija = self.glava
        while iteracija is not None:
            print(iteracija.element)
            iteracija = iteracija.next

if __name__ == '__main__':
    stog = Stog()
    stog.push(4)
    stog.push(12)
    stog.push(89.3)
    stog.push(44.1)
    stog.pop()
    stog.ispis()
    stog.velicina()
    stog.top()
