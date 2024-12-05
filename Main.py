'''Redaccion de Ejercicios Navideños'''
import random

print('''1. Árbol de Navidad''')
def Arbol_navidad(numero_n):

    for i in range(numero_n):
        print(' ' * (numero_n - i - 1) + '*' * (2 * i + 1))

        # Parte inferior del rombo
    print("   |||")

Arbol_navidad(5)

print("2. Lista de regalos")
lista = ("Reloj Inteligente", "Revista", "Rompecabezas", "Riñonera"
         , "Ropa personalizada", "Ramo de flores", "Juego de mesa"
         , "Ribro", "Bono regalo")


def filtrar_regalos(lista:tuple):


    for encontrar in lista:
        if encontrar.startswith("R"):
            print("Regalo: ",encontrar)


filtrar_regalos(lista)
bolitas=(5,4,2,1,12,3,51,2,5,2,1,4,7,5,3,2,4,3,4,3,6,5,6,7,7,77,7876)
print("3. Contando bolas de nieve")
def contar_bolas(lista)->int:
    contadorcito=0
    for bolitas in lista:
        if bolitas>=5:
            contadorcito=contadorcito+1
    return contadorcito

print("Hay",contar_bolas(bolitas),"bolas de nieve gigantescas")
lista_nombre=("Pepe","Antonio","Jose","Paco","Fran","Jaime")
lista_premios=(1000,1233,5,1.12,3213,0)
print("4. Sorteo de Navidad")
def sorteo_navidad(lista_nombre, lista_premios):
    lista_resultado=[]
    for i in range(0,6):
        random.shuffle(lista_resultado)
        lista_resultado.append((lista_nombre[i],lista_premios[i]))
    return lista_resultado

print(sorteo_navidad(lista_nombre,lista_premios))
