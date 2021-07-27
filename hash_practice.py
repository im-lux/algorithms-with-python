def hashiraj(vrijednost, tabela):
    if tabela[vrijednost] == 0:
        tabela[vrijednost] = vrijednost

if __name__ == '__main__':
    lista = [29, 23, 14, 5, 15, 10, 3, 18, 1, 55, 99, 7, 100]
    hashTabela = [0] * 101
    # for i in range(len(hashTabela)):
    #     for j in range(len(lista)):
    #         if i == lista[j]:
    #             hashTabela[i] = lista[j]
    for i in range(len(lista)):
        hashiraj(lista[i], hashTabela)

    print(hashTabela)




def hash(vrijednost, tabela):
    suma = 0
    for x in vrijednost:
        suma += ord(x)
    modulo = suma % 20
    while(tabela[modulo] is not None):
        print("pokušaj haširanja",vrijednost,"na slot",modulo)
        print("kolizija kod haširanja",vrijednost)
        modulo += 1
    tabela[modulo] = vrijednost
    print(vrijednost, "se uspješno hašira na slot", modulo)

if __name__ == '__main__':
    lista = ["Marko", "Ante", "Marija", "Petar", "Ivan", "Filip", "Ljubo","Katja","Marina","Markov","Ljubo","Ljubo"]
    tabela = [None] * 20
    for i in range(len(lista)):
        hash(lista[i], tabela)
    print(tabela)




class Node:
    def __init__(self,value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.glava = None

    def insert(self,vrijednost):
        cvor = Node(vrijednost)
        cvor.next = self.glava
        self.glava = cvor

    def printaj(self):
        iteracija = self.glava
        while iteracija is not None:
            print(iteracija.value,end=" ")
            iteracija = iteracija.next

if __name__ == '__main__':
    lista = ['29', '23', '14', '5', '15', '10', '3', '18', '1', '16', '19', '36', '46']
    tabela = []
    for i in range(10):
        tabela.append(LinkedList())

    for i in range(len(lista)):
        suma = 0
        for element in lista[i]:
            suma += ord(element)
        modulo = suma % 9
        if tabela[modulo].glava is None:
            tabela[modulo].glava = Node(lista[i])
            tabela[modulo].glava.next = None
        else:
            cvor = Node(lista[i])
            cvor.next = tabela[modulo].glava
            tabela[modulo].glava = cvor

    for i in range(len(tabela)):
        print("Adresa",i,": kljucevi:",end=" ")
        tabela[i].printaj()
        print()



def omjer(lista, n):
    mapa = {}
    for i in range(len(lista)):
        for j in range(len(lista)):
            if (lista[i] + lista[j] == n) and i != j:
                # print("par vrijednosti koji daju broj",n,"je",lista[i]," i ",lista[j])
                if lista[i] > lista[j]:
                    mapa[lista[i]] = lista[j]
                else:
                    mapa[lista[j]] = lista[i]
    return mapa

if __name__ == '__main__':
    A = [1, 4, 45, 6, 10, 8]
    n = 16
    mapa = omjer(A,n)
    print(mapa)