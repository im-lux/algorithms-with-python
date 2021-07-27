#PREDAVANJE EUKLIDOV
# def nzm(a, b):
#     if b == 0:
#         return a
#     else:
#         print(a, b)
#         return nzm(b, a % b)
#
# xy = nzm(22,8)
# print(xy)

#PREDAVANJE FAKTORIJEL
# def faktorijel(a):
#     if a == 0:
#         return 1
#     else:
#         return a * faktorijel(a-1)
#
# xy = faktorijel(5)
# print(xy)

#PREDAVANJE BINARNO TRAŽENJE - BEZ REKURZIJE
# def binarno(lista, element):
#     lista = sorted(lista)
#     xvar = len(lista)
#     pola = xvar // 2
#     if element == lista[pola]:
#         return pola
#     elif element > lista[pola]:
#         while pola < len(lista):
#             if element == lista[pola]:
#                 return pola
#             else:
#                 pola += 1
#         pola = xvar // 2
#     else:
#         while pola > -1:
#             if element == lista[pola]:
#                 return pola
#             else:
#                 pola -= 1
#
#
# lista = [3, 56, 1, 4, 22, 5, 45, 11, 23]
# xy = int(input("Unesi broj: "))
# rez = binarno(lista, xy)
# print("broj je nađen na lokaciji", rez)

#PREDAVANJE BINARNO TRAŽENJE - REKURZIJA
# def binarno(lista, element, min, max):
#     if max < min:
#         return False
#     else:
#         srednji = (max+min) // 2
#         if element == lista[srednji]:
#             return srednji
#         elif element < lista[srednji]:
#             return binarno(lista, element, 0, srednji-1)
#         else:
#             return binarno(lista, element, srednji+1, max)
#
#
# lista = [5, 3, 1, 77, 43, 2, 12, 76, 70]
# lista = sorted(lista)
# print(lista)
# xy = int(input("Unesi broj: "))
# rez = binarno(lista, xy, 0, len(lista)-1)
# print(rez)

#1. ZADATAK AUDITORNE
# def sumiranje(lista, a):
#     if a == 0:
#         return 0
#     else:
#         return lista[a-1] + sumiranje(lista, a-1)
#
# lista = [1,2,3,4,5,7,8,9,10,34,56,9]
# a = len(lista)
# rez = sumiranje(lista, a)
# print(rez)

#2. ZADATAK AUDITORNE
# def potencija(x,n):
#     if n == 0:
#         return 1
#     else:
#         return x * potencija(x, n-1)
#
# x = 15
# n = 4
# rez = potencija(x,n)
# print(rez)

#1. ZADATAK LAB
# def zbroj(lista,x):
#     if x == 0:
#         return 0
#     else:
#         return lista[x-1] + zbroj(lista, x-1)
#
# lista = [4, 7, 11, 23, 8, 10]
# a = len(lista)
# xy = zbroj(lista, a)
# print(xy)

#2. ZADATAK LAB
# def preokreni(lista,tmplista,x):
#     if x == 0:
#         tmplista.append(lista[0])
#     else:
#         tmplista.append(lista[x])
#         preokreni(lista,tmplista,x-1)
#     return tmplista
#
#
# lista = [1,2,3,4,5]
# tmplista = []
# x = len(lista)-1
# xy = preokreni(lista,tmplista,x)
# print(xy)

#3. ZADATAK
# def palindrom(tekst, pomoc,x):
#     if x == len(tekst)-1:
#         pomoc += tekst[len(tekst)-1]
#     else:
#         pomoc += (tekst[x])
#         palindrom(tekst,pomoc,x+1)
#
#     print("tekst: ", tekst)
#     print("pomoc: ", pomoc)
#
#     if tekst == pomoc:
#         return True
#     else:
#         return False
#
# tekst = "lukul"
# pomoc = ""
# x = len(tekst)-1
# xy = palindrom(tekst,pomoc,0)
# print(xy)
# def palindrom(tekst, pomoc,x):
#     if x == 0:
#         pomoc += tekst[0]
#     else:
#         pomoc += (tekst[x])
#         palindrom(tekst,pomoc,x-1)
#
#     print("tekst: ", tekst)
#     print("pomoc: ", pomoc)
#
#     if tekst == pomoc:
#         return True
#     else:
#         return False
#
# tekst = "ja sam"
# pomoc = ""
# x = len(tekst)-1
# xy = palindrom(tekst,pomoc,x)
# print(xy)

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# if __name__ == '__main__':
#     ukupno = fib(4)
#     print(ukupno)

#3. ZADATAK LAB
def palindrom(string):
    if len(string) < 1:
        return True
    else:
        if string[0] == string[len(string)-1]:
            return palindrom(string[1:len(string)-1])
        else:
            return False

if __name__ == '__main__':
    string = "ja sam lux"
    nekaj = palindrom(string)
    print(string)
    print(nekaj)

