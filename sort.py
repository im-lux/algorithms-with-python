class Gomila:
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def percDown(self,i):
        while (i*2) <= self.size:
            pomoc = self.minChild(i)
            if self.heapList[i] > self.heapList[pomoc]:
                xvar = self.heapList[i]
                self.heapList[i] = self.heapList[pomoc]
                self.heapList[pomoc] = xvar
            i = pomoc

    def minChild(self,i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHeap(self,lista):
        i = len(lista) // 2
        self.size = len(lista)
        self.heapList = [0] + lista[:]
        while i > 0:
            self.percDown(i)
            i = i - 1

def napraviListu(gomila,lista,n):
    for i in range(n):
        lista[i] = gomila.heapList[i+1]

if __name__ == '__main__':
    lista = [12,11,13,5,6,7]
    print(lista)
    n = len(lista)
    gom = Gomila()
    gom.buildHeap(lista)
    napraviListu(gom,lista,n)
    print(lista)
    lista2 = [7, 77, 78, 87, 4, 435, 2, 11]
    velicina = len(lista2)
    heap = Gomila()
    heap.buildHeap(lista2)
    napraviListu(heap, lista2, velicina)
    print('nova lista - sortirana ', lista2)
