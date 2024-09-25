def es_primo(numero):
    if numero <= 1:
        devolver = False
    elif numero == 2:
        devolver = True
    elif numero%2 == 0:
        devolver = False
    else:
        devolver = True
        contador = 3
        contador_primo = 0
        while contador<numero and contador_primo==0:
            if numero%contador==0:
                contador_primo+=1
                devolver = False
            contador += 2
    return devolver

def filtrar_primos(numeros, menor_numero):
    numeros.sort()

    lista_filtrada = []
    numeros_primos_mayores = 0
    indice = -1
    contador = 1
    while numeros_primos_mayores < 2 and len(numeros) >= contador:
        if es_primo(numeros[indice]) and numeros[indice]>menor_numero:
            numeros_primos_mayores +=1
            lista_filtrada.append(numeros[indice])
        indice -= 1
        contador += 1
    lista_filtrada.sort()
    return lista_filtrada


def ordenar_por_longitud_de_tuplas(tuplas):
    lista_len = []
    for tupla in tuplas:
        lista_len.append(len(tupla))
    lista_len.sort(reverse=True)

    lista_filtrada = []
    for l in lista_len:
        condicion = False
        indice = 0
        while not condicion and indice<= len(tuplas):
            if l == len(tuplas[indice]):
                lista_filtrada.append(tuplas[indice])
                condicion = True
            indice +=1 

                
    return lista_filtrada

def concatenar_primeros_elementos(lista):
    lista_filtrada = []
    for li in lista:
        lista_filtrada.extend(li[0:3])
    return lista_filtrada

#   matriz[i][j]

def mayor_anteriores(matriz):
    matriz_filtrada = []
    for elem in matriz:
        fila = [False] * len(elem)
        matriz_filtrada.append(fila)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            numero_actual = matriz[i][j]
            if i==0 and j==0:
                matriz_filtrada[i][j] = True
            else:
                condicion_fila = True
                condicion_columna = True
                #por fila
                long_fila = 0
                while condicion_fila and long_fila < j:
                    if matriz[i][long_fila] > numero_actual:
                        condicion_fila = False
                    long_fila += 1
                #por columna
                long_colum = 0
                while condicion_columna and long_colum < i:
                    if matriz[long_colum][j] > numero_actual:
                        condicion_columna = False
                    long_colum += 1

                matriz_filtrada[i][j] = condicion_fila and condicion_columna
    return matriz_filtrada

            
matriz= [[1,4,5,3], 
         [2,3,4,5], 
         [1,4,4,6]]

print(mayor_anteriores(matriz)) #  [[True,True,True,False],
                                #   [True,False,False,True],
                                #   [False,True,False,True]]


