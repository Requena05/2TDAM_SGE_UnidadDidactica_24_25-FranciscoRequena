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
'''Crea una función llamada cuenta_regresiva que reciba un número n y haga una
cuenta regresiva desde ese número hasta 1. Por cada número, imprime "�����" si es
divisible por 3, "�������" si es divisible por 5, y "����" si es divisible por ambos.'''

print("5. Cuenta regresiva de Año Nuevo")
def cuenta_regresiva(numero):

    for n in range(numero,0,-1):
        if (n%3 ==0):
            print(n,"🎡")
        if(n%5 == 0 ):
            print(n,"🎄")
        if(n%3 ==0 and n%5==0):
            print(n,"🎁")

cuenta_regresiva(12)
'''Escribe una función llamada sec_natal que reciba una lista de tuplas con el nombre de
una persona y su edad, y devuelva una lista con el nombre de las personas mayores de
edad (18 años o más). La lista debe estar ordenada de forma alfabética'''

print("6. Secuencia de Navidad")

def sec_natal( lista: list):

    lista_mayores: list = []

    for datos in lista:
        if datos[1]>17:
           lista_mayores.append(datos[0])

    lista_mayores.sort()

    print(lista_mayores)



sec_natal([("paco",12),("Jose",23),("Pedro",55),("Victor",18)])

'''7. Resolución de Sudoku (sin usar bibliotecas externas)
Crea una función llamada resolver_sudoku que reciba una lista de listas representando
un tablero de Sudoku incompleto, con ceros (0) representando las casillas vacías. La
función debe intentar resolver el Sudoku, devolviendo el tablero resuelto. Si no es
posible resolver el Sudoku con los valores proporcionados, la función debe devolver
None. El Sudoku debe respetar las reglas:
1. Cada fila debe contener los números del 1 al 9 sin repetirse.
2. Cada columna debe contener los números del 1 al 9 sin repetirse.
3. Cada una de las 9 subcuadrículas de 3x3 debe contener los números del 1 al 9
sin repetirse.'''


def resolver_sudoku(tablero):
    def es_valido(num, fila, col):
        for columna in range(9):
            if tablero[fila][columna] == num:
                return False
        for filas in range(9):
            if tablero[filas][col] == num:
                return False
        inicio_fila = (fila // 3) * 3
        inicio_col = (col // 3) * 3
        for r in range(inicio_fila, inicio_fila + 3):
            for c in range(inicio_col, inicio_col + 3):
                if tablero[r][c] == num:
                    return False
        return True
    def resolver():
        for fila in range(9):
            for col in range(9):
                if tablero[fila][col] == 0:
                    for num in range(1, 10):
                        if es_valido(num, fila, col):
                            tablero[fila][col] = num
                            if resolver():
                                return True
                            tablero[fila][col] = 0
                    return False
        return True
    if resolver():
        tablero_resuelto=tablero
        return print("\n",tablero_resuelto)
    else:
        return None

tablero_incompleto=[
    [5, 3, 4, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

resolver_sudoku(tablero_incompleto)

