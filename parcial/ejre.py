def es_letra(letra):
    return letra.isalpha()
def es_acento(letra, clave_m_or_M):
    dicc_acentos = {'m':['à','è','ì','ò','ù']}
    condicion = False
    indice  = 0
    while not condicion and indice < len(dicc_acentos[clave_m_or_M]):
        if dicc_acentos[clave_m_or_M][indice] == letra:
            condicion = True
        indice += 1
    return condicion

def contar(cadena):
    lista = []
    for e in cadena:
        if es_letra(e):
            e = e.lower()
            if (not es_acento(e,'m')):
                if e not in lista:
                    lista += e
    return len(lista)

lista_1 = ["museos", "senderismo", "bares", "montañismo"]
lista_2 = ["bares", "museos", "senderismo", "conciertos"]
lista_3 = ["bares", "conciertos", "museos"]

def elegir(atracciones, actividades_deseadas, costo_promedio):
    MAX_COSTO = 8000
    devolver = False
    if costo_promedio <= MAX_COSTO:    
        condicion = 0
        i = 0 
        while condicion < 3 and i < len(atracciones):
            es_igual = False
            j = 0
            while not es_igual and j < len(actividades_deseadas):
                if actividades_deseadas[j] == atracciones[i]:
                    es_igual = True
                    condicion += 1
                else:
                    j += 1
            i += 1
        if condicion == 3:
            devolver = True
    return devolver

print(elegir(lista_1, lista_2, 5000))
print(elegir(lista_1, lista_3, 10000))

#camino a la fama
lista = [['Luisa', 4], ['Mariano', 10], ['Luisa', 5]]
def procesar_lista(lista):
    dicc = {}
    for clave,puntaje in lista:
        if clave not in dicc:
            dicc[clave] = [puntaje, 1, 1]
        else:
            dicc[clave][0] += puntaje
            dicc[clave][1] += 1
        dicc[clave][2] = dicc[clave][0] / dicc[clave][1]
    return dicc
def ordernar_mayor_menor(dicc):
    ordenados = sorted(dicc.items(), key = lambda item : item[1][2], reverse = True)
    return ordenados
def listar(lista):
    for e in lista:
        print(f"{e[0]}         {e[1][2]:.1f}")


listar(ordernar_mayor_menor(procesar_lista(lista)))
    



