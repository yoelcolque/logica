def algo(palabra):
    palabra = "palaibras"
    indice = 0
    condion = True
    while len(palabra)>indice and condion:
        if palabra[indice] == 'i':
            condion = False
        indice += 1
    inicio = 0
    while (len(palabra) > inicio and palabra[inicio] != 'i'):
        print(palabra[inicio])
        inicio +=1

def es_binario(cadena):
    condicion = True
    indice = 0
    while len(cadena)>indice and condicion:
        if cadena[indice] != '0' and cadena[indice] != '1':
            condicion = False
        indice += 1
    return condicion


3) Escribir una función que reciba una dirección de mail, y devuelva True ó False, en función de haber
evaluado que dicha dirección está bien formada.
Escribir una función que reciba una cadena de caracteres que representa una dirección de mail. La
función deberá devolver True ó False, en función de haber evaluado que dicha dirección está bien
formada.
Se debe controla que:
a. Que no contenga blancos
b. Que sólo se utilicen letras y/o números para la parte del nombre, delante de la @
c. Que haya exactamente una arroba
d. Que los nombres de dominio sean: fi.uba.ar ó gmail.com