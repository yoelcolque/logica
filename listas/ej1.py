#es primo por 
def es_primo(num):
    if num == 2:
        devolver = True
    if num < 2 or num % 2 == 0:
        devolver = False
    if num > 1:
        devolver = True
        contador = 3
        while num%contador== 0:
            devolver += 1
            if num%contador == 0:
                devolver = False 
    return devolver

## WHILE
def filtrar_primos(lista, num):
    lista_filtrada = []
    for valor in lista:
        if valor > num and es_primo(valor):
            lista_filtrada.append(valor)
    return lista_filtrada

def ordenar_por_longitud_de_tuplas(lista_de_tuplas):
    lista_datos = []
    for tupla in lista_de_tuplas:
        lista_datos.append(len(tupla))
        lista_datos.sort()

    lista_ordenada_por_longitud = []
    index = 0
    for tupla in lista_de_tuplas:
        if  len(tupla) == lista_datos[index]:
            lista_ordenada_por_longitud.append(tupla)
        index += 1    
    return lista_ordenada_por_longitud 

def concatenar_primeros_elementos (lista_base):
    lista_a_concatenar = []
    for lista in lista_base:
        condicion = 0
        while condicion < 2:
            lista_a_concatenar.append(lista[condicion])
            condicion += 1        
    return lista_tres_primeros_por_lista

def mayores_anteriores (matris):
    #matris 3x4
    matris_booleana = []
    for lista in matris:
        lista_booleana = []
        for num in lista:
            if es_mayor_anterior_por_lista(lista, num) and es_mayor_anterior_por_matris(lista,matris,num):
                condicion = True
            else:
                condicion = False
            lista_booleana.append(condicion)
        matris_booleana.append(lista_booleana)
    return matris_booleana



def es_mayor_anterior_por_lista(lista, num):   
    index = lista.index(num)
    devolver = True
    while index>= 0 and lista[index] <= num:
        index -= 1
        if num < lista[index]:
            devolver = False
    return devolver



#matris 3x4
def es_mayor_anterior_por_matris(lista,matris,num):
    index_lista = matris.index(lista)
    index = lista.index(num)

    devolver = True
    while index_lista >= 0 and matris[index_lista][index] <= num:
        index_lista -=1
        if matris[index_lista][index] > num:
            devolver = False
    return devolver


matris = [[1,4,5,3], 
         [2,3,4,5], 
         [1,4,4,6]]

print(mayores_anteriores(matris))


















