def solicitar_valor(text):
    return int(input(text))
def imprimir_num(num):
    return print(num)
def es_cero(num):
    return num == 0
def es_par(num):
    return num%2==0
def ordenar_lista(lista):
    return lista.sort()
def devolver_lista_sin_repedidos(lista):
    return list(set(lista))

def crear_lista():
    lista = []
    num = solicitar_valor("Ingrese numero: ")
    contador_par = 0
    while not es_cero(num) and contador_par <=3:
        imprimir_num(num)
        lista.append(num)
        num = solicitar_valor("Ingres numero: ")
        if es_par(num):
            contador_par +=1
    lista_pares = lista[::2]
    nueva_lista = devolver_lista_sin_repedidos(lista_pares)
    return nueva_lista


print(crear_lista())