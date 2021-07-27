class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def visina(root):
    if root is None:
        return 0
    else:
        lijevi = visina(root.left)
        desni = visina(root.right)
        if lijevi > desni:
            return lijevi+1
        else:
            return desni+1

#obican binary tree, elementi se dodaju u tree onako kako su poredani u listi (ne-sortirani)
def listaUBinaryTree(lista, root, prvi, velicina):
    if prvi < velicina:
        root = Node(lista[prvi])
        root.left = listaUBinaryTree(lista, root.left, 2 * prvi + 1, velicina)
        root.right = listaUBinaryTree(lista, root.right, 2 * prvi + 2, velicina)
    return root

def insert(root, node):
    if root is not None:
        if node.value > root.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def search(root,vrijednost):
    if root is not None:
        if root.value == vrijednost:
            return True
        else:
            if vrijednost > root.value:
                return search(root.right, vrijednost)
            else:
                return search(root.left, vrijednost)
    return False

def minValue(root,broj=10000):
    if root is not None:
        if root.value < broj:
            broj = root.value
        return minValue(root.left, broj)
    return broj

def maxValue(root,broj=-10000):
    if root is not None:
        if root.value > broj:
            broj = root.value
        return maxValue(root.right, broj)
    return broj

def deleteNode(root,node):
    if root is not None:
        if node.value < root.value:
            root.left = deleteNode(root.left, node)
        elif node.value > root.value:
            root.right = deleteNode(root.right, node)
        else:
            if root.left is None:
                uzmi = root.right
                root = None
                return uzmi
            elif root.right is None:
                uzmi = root.left
                root = None
                return uzmi
            najmanji = minValue(root.right)
            root.value = najmanji.value
            root.right = deleteNode(root.right, najmanji.value)
        return root

def dodajUListu(root, lista=[]):
    if root is not None:
        dodajUListu(root.left)
        lista.append(root.value)
        dodajUListu(root.right)
    return lista

def sortListe(lista):
    for i in range(len(lista)):
        najmanji = i
        for j in range(i+1, len(lista)):
            if lista[najmanji] > lista[j]:
                najmanji = j
        lista[i], lista[najmanji] = lista[najmanji], lista[i]

def dodajUBST(root,lista):
    if root is not None:
        dodajUBST(root.left,lista)
        root.value = lista[0]
        lista.pop(0)
        dodajUBST(root.right,lista)

def dodajUStablo(lista):
    root = Node(lista[0])
    for i in range(1, len(lista)):
        insert(root,Node(lista[i]))
    return root


def pronalazakLijevo(root,element,brojac):
    if root is not None:
        if root.left is not None and root.left.value == element:
            brojac += root.value
        if root.right is not None and root.right.value == element:
            brojac += root.value
        return pronalazakLijevo(root.left, element, brojac)
    return brojac

def pronalazakDesno(root,element,brojac):
    root = root.right
    if root is not None:
        if root.left is not None and root.left.value == element:
            brojac += root.value
        if root.right is not None and root.right.value == element:
            brojac += root.value
        return pronalazakDesno(root.right, element, brojac)
    return brojac

def je_bsp(lista):
    if type(lista) is not list:
        return True
    lijevi, desni = lista[1], lista[2]
    if type(lista[1]) is list:
        lijevi = lista[1][0]
    if type(lista[2]) is list:
        desni = lista[2][0]
    if lista[0] < lijevi or lista[0] > desni:
        return False
    return je_bsp(lista[1]) and je_bsp(lista[2])

def printInOrder(root):
    if root is not None:
        printInOrder(root.left)
        print(root.value)
        printInOrder(root.right)

def printPreOrder(root):
    if root is not None:
        print(root.value)
        printPreOrder(root.left)
        printPreOrder(root.right)

def printPostOrder(root):
    if root is not None:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root.value)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(visina(root))
    print('---')
    printInOrder(root)
    print('---')
    printPreOrder(root)
    print('---')
    printPostOrder(root)
    print('---')
    lista = [1,2,3,4,5,6,6,6,6,6]
    korijen = None
    korijen = listaUBinaryTree(lista, korijen, 0, len(lista))
    printInOrder(korijen)
    print('---')
    cvor = Node(100)
    insert(cvor, Node(30))
    insert(cvor, Node(500))
    insert(cvor, Node(10))
    insert(cvor, Node(20))
    printInOrder(cvor)
    print(search(cvor, 100))
    print(minValue(cvor))
    print(maxValue(cvor))
    print('---')
    deleteNode(cvor, Node(30))
    printInOrder(cvor)
    print('-----')
    stablo = Node(10)
    stablo.left = Node(2)
    stablo.right = Node(7)
    stablo.left.left = Node(8)
    stablo.left.right = Node(4)
    lista = dodajUListu(stablo)
    printInOrder(stablo)
    print(lista)
    sortListe(lista)
    print(lista)
    dodajUBST(stablo, lista)
    printInOrder(stablo)
    print('-----')
    drvo = Node(4)
    drvo.left = Node(2)
    drvo.right = Node(5)
    drvo.left.left = Node(7)
    drvo.left.right = Node(2)
    drvo.right.left = Node(2)
    drvo.right.right = Node(3)
    printInOrder(drvo)
    brojac = 0
    ukupno = pronalazakLijevo(drvo,2, brojac) + pronalazakDesno(drvo, 2, brojac)
    print("ukupno",ukupno)
    print(je_bsp([50, [44, 30, 48], [49, [66, 60, 67], 88]]))
