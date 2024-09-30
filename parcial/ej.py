def es_longitud(palabra):
    return len(palabra)>= 8 and len(palabra)<=12
def es_mayuscula(letra):
    return letra.isupper()
def es_acento(letra,clave_m_or_M):
    tupla_acentos= {'m' : ('á','é','í','ó','ú'), 'M' : ('Á','É','Í','Ó','Ú')}
    return letra in tupla_acentos[clave_m_or_M]
def es_numero(letra):
    return letra.isdigit()
def es_caracter_especial(letra):
    caracter_especial = ['*','-','$','@']
    condicion = False
    indice = 0
    while not condicion and indice < len(caracter_especial):
        if letra in caracter_especial:
            condicion = True
        indice += 1
    return condicion
def es_letra(letra):
    return letra.isalpha()

def validar(palabra):
    if es_longitud(palabra):
        indice = 0
        condicion = True
        numero = 0
        letra_M = 0
        letra_m = 0
        while condicion and indice < len(palabra):
            letra = palabra[indice]
            if es_letra(letra):
                if es_mayuscula(letra):
                    letra_M +=1
                    if es_acento(letra, 'M'):
                        condicion = False
                else:
                    letra_m += 1
                    if es_acento(letra, 'm'):
                        condicion = False
            elif es_numero(letra):
                numero += 1 
            else:
                if not es_caracter_especial(letra):
                    condicion = False
            indice += 1
        if not (letra_M > 0 and letra_m > 0 and numero > 0):
            condicion = False
    else:
        condicion = False
    return condicion        


lista_1 = ["natación", "gimnasio", "voley", "futbol"]
lista_2 = ["natación", "voley", "gimnasio"]
lista_3 = ["natación", "futbol", "karate"]
MAX_CUOTA = 8000
def elegir(actividades, actividades_deseadas, cuota):
    devolver = False
    if cuota <= MAX_CUOTA:
        i = 0
        j = 0
        contador = 0
        while i < len(actividades) and contador < 2:
            if j < len(actividades_deseadas):
                if actividades[i] != actividades_deseadas[j]:
                    j += 1
                else:
                    i +=1
                    j = 0
                    contador += 1
            else:
                i += 1
                j = 0
        if contador == 2:
            devolver = True
    return devolver

print(elegir(lista_1, lista_2, 5000)) #--->  True si 5000 <= MAX_CUOTA
print(elegir(lista_1, lista_3, 5000)) #--->  True si 5000 <= MAX_CUOTA
print(elegir(lista_2, lista_3, 100)) #--->  False

# Función para procesar la lista de votaciones y generar el diccionario con total de votos
def procesar_votaciones(votacion):
    total_votos = {}
    
    for mesa in votacion:
        partido = mesa[0]
        diputados = mesa[1]
        senadores = mesa[2]
        votos_totales = diputados + senadores
        
        if partido in total_votos:
            total_votos[partido] += votos_totales
        else:
            total_votos[partido] = votos_totales
    
    return total_votos

# Función para ordenar los partidos por total de votos
def listar_partidos_por_votos(total_votos):
    partidos_ordenados = sorted(total_votos.items(), key=lambda x: x[1], reverse=True)
    return partidos_ordenados

# Ejemplo de uso
votacion = [
    ["PP", 19, 35],
    ["PSOE", 20, 30],
    ["VOX", 15, 15],
    ["PP", 0, 15]
    # Agregar más mesas según sea necesario
]

# Procesar la lista de votaciones
total_votos = procesar_votaciones(votacion)

# Listar los partidos ordenados por votos
partidos_ordenados = listar_partidos_por_votos(total_votos)

print(partidos_ordenados)
# Mostrar los resultados
for partido, votos in partidos_ordenados:
    print(f"{partido}: {votos} votos")




