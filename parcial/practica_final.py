def validar(palabra):
    condicion = True
    i = 0
    letra_M = 0
    letra_m = 0
    numero = 0
    caracter_especial = 0
    while condicion and i < len(palabra):
        letra = str(palabra[i])
        if letra.isalpha():
            if letra.isupper():
                letra_M += 1
                if letra in ['À','È','Ì','O','U']:
                    condicion = False
            elif not letra.isupper():
                letra_m += 1 
                if letra in ['à','è','ì','ò','ù']:
                    condicion = False
        elif letra.isdigit():
            numero += 1
        elif letra in ['*','-','$','@']:
            caracter_especial += 1
        else:
            condicion = False
        i += 1
    return (condicion and letra_M > 0 and letra_m > 0 and numero > 0 and caracter_especial > 0)
        
 


def elegir(actividades, actividades_deseadas, cuota):
    MAX_CUOTA = 8000
    i = 0
    condicion = 0
    devolver = False
    if cuota <= MAX_CUOTA:
        while i < len(actividades) and condicion < 2:
            j = 0
            es_igual = False
            while j < len(actividades_deseadas) and not es_igual:
                if actividades[i] == actividades_deseadas[j]:
                    es_igual = True
                    condicion += 1
                j += 1
            i += 1
        if (condicion == 2):
            devolver = True    
    else:
        devolver = False
    return devolver

lista_1 = ['natación', 'gimnasio', 'voley', 'futbol']
lista_2 = ['natación', 'voley', 'gimnasio']
lista_3 = ['natación', 'futbol', 'karate']

def procesar_lista(lista):
    dicc = {}
    for e in lista:
        clave = e[0]
        total_votos = e[1] + e [2]
        if clave not in dicc:
            dicc[clave] = total_votos
        else:
            dicc[clave] += total_votos
    return dicc

def listar_partidos(dicc):
    ordenados = sorted(dicc.items(), key = lambda item : item[1], reverse = False)
    for e in ordenados:
        print(f"{e[0]}      {e[1]}")








def contar(palabra):
    lista = []
    for letra in palabra:
        if letra.isalpha():
            letra = letra.lower()
            if letra not in ['à','è','ì','ò','ù'] and letra not in lista:
                lista.append(letra)
    return len(lista)

print(contar("Aaaaàb"))
print(contar("%_123 3*"))
print(contar("Algoritmos y Programaciòn 1"))


def elegir(actividades, actividades_deseadas, costo):
    MAX_COSTO = 8000
    devolver = False
    if costo <= MAX_COSTO:
        condicion = 0
        i = 0
        while condicion < 3 and i < len(actividades):
            j = 0
            while condicion < 3 and j < len(actividades_deseadas):
                if actividades[i] == actividades_deseadas[j]:
                    condicion += 1
                j += 1
            i += 1
        if condicion == 3:
            devolver = True      
    return devolver

def procesar_lista(listas):
    dicc = {}
    for lista in listas:
        clave = lista[0]
        puntaje = lista[1]
        catidad_puntajes = 1
        if clave not in dicc:
            dicc[clave] = [puntaje, catidad_puntajes, puntaje]       
        else:
            dicc[clave][0] += puntaje
            dicc[clave][1] += 1
            dicc[clave][2] = dicc[clave][0] / dicc[clave][1]
    return dicc

def listar_mayor_a_menor(dicc):
    ordenados = sorted(dicc.items(), key = lambda item : item[1][2], reverse = True)
    print(ordenados)
    for tupla in ordenados:
        print(f"{tupla[0]}      {tupla[1][2]}")


lista = [ ['Luisa', 4], ['Mariano', 10], ['Luisa', 5]]

listar_mayor_a_menor(procesar_lista(lista))