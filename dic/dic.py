libros = {
" El Aleph.": "Borges" ,
"Sobre Heroes y Tumbas.":"E.Sabato",
"La Gesta del Marrano":" M. AGUINIS",
"Misteriosa Buenos Aires.": "Mujica Laines",
"Fundacion":"I.Asimov"
}

def imprimir_autores (libros):
    for clave in libros:
        print(libros[clave])


torneos = {'Racing': [18], 'ROSARIO': 5, 'FERRO': 2}

def numero_veces_letra_in_palabra (palabra):
    dic_letras_num = {}
    for l in palabra:
        if l not in dic_letras_num:
            dic_letras_num[l] = 1
        else:
            dic_letras_num[l] += 1
    return dic_letras_num


alumnos={171717:('Lopez',[9,10],('llopez@fi.uaba.ar','lopecito77@gmail.com'))}

alumnos[171717][1].append(8)


stock={1:[2,300],2:[5000,3],5:[60,400]}

def suma_inventario(stock):
    valor = 0
    for clave in stock:
        valor += stock[clave][0] * stock[clave][1]
    return valor


alumnos={37954018:'Lopez',6338:'Juarez', 98231496:'Uriel'}
print(alumnos.pop(6338), "Esto es por pop, elimina elemento por clave")
print(alumnos)
print(sorted(alumnos.keys()), "Esto es por keys  ")
print(sorted(alumnos.values()), "Esto es por valor ")
print(sorted(alumnos.items()), "Esto es por item, devuelve los pares de dic en tuplas ")





precios = {"banana": 50,"manzana": 28,"nananja": 15,"pera": 30}
stock = {"banana": 60, "manzana": 0, "nananja": 32, "pera": 15}

for clave_precios, clave_stock in zip(precios,stock):
    print('La fruta ', clave_precios, 'vale ', precios[clave_precios], 'y su stock es de: ', stock[clave_stock])


producto=['ctacte', 'cajaahorro','prestamo','plazofiijo']
codigo=[1,2,3,4]

dict(zip(producto,codigo))



precios = {"banana": 50,"manzana": 28,"nananja": 15,"pera": 30}
stock = {"banana": 60, "manzana": 0, "nananja": 32, "pera": 15}

total = 0
for clave, clave2 in zip(precios,stock):
    total_parcial = 0
    total += precios[clave] * stock[clave]
    print('Este es el total_parcial de la fruta: ',precios[clave] * stock[clave])
print('Este es el total: ',total)



precios = {"banana": 50,"manzana": 28,"nananja": 15,"pera": 30}
stock = {"banana": 60, "manzana": 0, "nananja": 32, "pera": 15}

total1 = 0
for frutas in zip (precios, stock):
    total1 = total1 + precios[frutas[0]] * stock[frutas[0]]
    print(frutas[0],'valor total', precios[frutas[0]] * stock[frutas[0]])
print ("Monto Final:",total1)




descripciones=[(1,'Martillo'),(2,'tornillo'),(5,'mechas')]
stock={1:[2,300],2:[5000,3],5:[60,400]}

total = 0 
for tupla in descripciones:
    print(tupla[1],'su valor parcial es: ', stock[tupla[0]][0] * stock[tupla[0]][1] )
    total +=  stock[tupla[0]][0] * stock[tupla[0]][1]
print(total)


dict_equipo_puntaje = {}

#solicitar_valor
def solicitar_valor(text):
    valor = input(text)
    return valor
#crear_tabla
def crear_tabla(dicc):
    print('si quiere salir de sistma escriba en nombre NO')
    nombre = 'SI'
    while nombre != 'NO':
        nombre = str(solicitar_valor('Ingrese nombre equipo: '))
        if nombre != 'NO':
            puntos = int(solicitar_valor('Ingrese puntos acumulados:'))

            if nombre not in dicc:
                dicc[nombre] = puntos
            else:
                dicc[nombre] += puntos
            dicc = ordenar_tabla_decreciente(dicc)
    return dicc
#ordenar_tabla_decreciente
def ordenar_tabla_decreciente(dicc):
    lista = []
    for clave in dicc:
        lista.append(dicc[clave])
    lista.sort(reverse= False)
    indice = 0
    for num in lista:
        for clave in dicc:
            if num == dicc[clave]:
                dicc[clave] = num
    return dicc