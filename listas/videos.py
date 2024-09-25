lista = [1,2,3,4]

lista = lista + [3,6,7]

print(lista)

print(lista.pop(1))
print(lista)

print(lista.count(3))

lista = [10,1,-3,8,23,18]
del(lista[2:4])
print(lista)


lista = []

#1
for e in range(1,101):
    lista.append(e**2)
#2
lista2 = [e**2 for e in range(1,101)]
#1 y 2 son igules en generar listas, el 2 es generar listas por compresion


lista_compresion = [[e,e**2,e**3] for e in range(1,6)]

print(lista_compresion)


lista_super = [['bana',9],['manz',5],['pera',6],['frut',8]]
print(lista_super)
lista_super.sort(key= lambda item:item[1])
print(lista_super)


suma = lambda x,y: x+y
print(suma(5,6))

lista = [7,2,3]
nueva_lista = [e**2 for e in lista]

lista = [1,2,3,4,5]
nueva_lista = list(filter(lambda item:item%2==0, lista))
print(nueva_lista)

nueva_lista = [e for e in lista if e%2==0]
print(nueva_lista)

sup_triangulo = lambda b,a : (b*a)/2
print(sup_triangulo(5,10))

v_c = ('i','u')
v_a = ('a','e','o')

def es_diptongo (palabra):
    condicion = False
    indice = 0
    while not condicion and indice < len(palabra) - 1:
        if (palabra[indice] in v_a and palabra[indice + 1] in v_c) or (palabra[indice] in v_c and palabra[indice+1] in v_c):
            condicion = True
        indice += 1
    return condicion


print("------------------------")
#crear lista de palabras, recibo text, return lista_palabras
def definir_palabras_de_text(text):
    return text.split()

#crear sublista [palabra,n veces], resivo lista_palabras, return sublista
def crear_sublista(lista_palabras):
    lista_anidada = [[e,lista_palabras.count(e)] for e in set(lista_palabras)]
    lista_anidada.sort(key = lambda e: e[1], reverse = True)
    return lista_anidada
#main
def main():
    text = "hola mundo como estas las estreliilantas dicen hola como estan"
    return crear_sublista(definir_palabras_de_text(text))



#1. Una lista que contenga los cuadrados de los múltiplos de 4, entre 4 y 20 inclusive.
lista = [16, 64, 144, 256, 400]

# create_list() -> return lista
def create_list(multiplo,max_evaluado):
    return [e**2 for e in range(multiplo, max_evaluado + 1) if e % multiplo == 0]
    
print(create_list(4,20))


#2. En base a la siguiente lista de notas: l_notas = [2, 2, 4, 9, 7, 10, 2, 5, 7] genere la lista
l_notas = [2, 2, 4, 9, 7, 10, 2, 5, 7]
def devolver_lista_aprobados (lista):
    return [e for e in l_notas if e >=7]
print(devolver_lista_aprobados(l_notas))

#3. En base a la siguiente lista de apellidos:
l_apellidos = ['Perez', 'Alvarez', 'Rodriguez', 'Alonso', 'García', 'Fernandez', 'Arias']
#Genere una lista de apellidos que comiencen con la letra “A”.
def devolver_lista_inicales_a (lista):
    return [e for e in l_apellidos if 'A' in e[0]]
print(devolver_lista_inicales_a(l_apellidos))
#La lista a obtener será: ['Alvarez', 'Alonso', 'Arias']

tupla = 5,6,4,7,8
tupla1 = (3,)
print(tupla)
print(tupla1)
print(tupla1 + tupla)

tupla = (2, 8, 23, 48, 5, 8)
posicion = 0
while posicion < len(tupla) and \
    tupla[posicion] % 2 == 0:
    print(tupla[posicion])
    posicion += 1
