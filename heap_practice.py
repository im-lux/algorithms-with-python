import heapq

class Gomila:
    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                pomoc = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = pomoc
            i = i // 2

    def insert(self,k):
        self.heapList.append(k)
        self.size = self.size + 1
        self.percUp(self.size)

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

    def delMin(self):
        xvar = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size = self.size - 1
        self.heapList.pop()
        self.percDown()
        return xvar

    def buildHeap(self,lista):
        i = len(lista) // 2
        self.size = len(lista)
        self.heapList = [0] + lista[:]
        while i > 0:
            self.percDown(i)
            i = i - 1

if __name__ == '__main__':
    listaBla = [3,5,9,6,8,20,10,12,18,9]
    gomila = Gomila()
    gomila.buildHeap(listaBla)
    gomila.insert(45)
    print(gomila.heapList)

    lista = [4, [5, [15, 16, 25], [9, 14, 12]], [6, [7, 11, 13], 20]]
    lista2 = []
    for i in lista:
        if isinstance(i, list):
            for j in i:
                if isinstance(j, list):
                    for k in j:
                        lista2.append(k)
                else:
                    lista2.append(j)
        else:
            lista2.append(i)
    print(lista2)
    heap = Gomila()
    heap.buildHeap(lista2)
    heap.insert(2)
    print(heap.heapList)

    lista3 = [1,3,9,7,5]
    hop = Gomila()
    hop.buildHeap(lista3)
    hop.insert(4)
    print(hop.heapList)
