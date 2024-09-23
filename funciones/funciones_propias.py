def devolver_nombre_mes_por_numero(numero):
    meses = ("ene","feb","mar","abril","may","jun","jul","ago","sep","nov","dic")
    if numero <= 0 or  numero > 12:
        devolver = "Mes Invalido"
    else:
        devolver = meses[numero - 1]

def es_anio_bisiesto(anio):
    return anio%4 == 0 or anio % 100 ==0 and anio % 400 == 0
def calcualar_dias_del_mes(mes,anio):
    dias = (31,28,31,30,31,30,31,31,30,31,30,31)
    if mes <= 0 or  mes > 12:
        devolver = "Mes Invalido"
    elif mes == 2 and es_anio_bisiesto(anio):
        devolver = 29
    else:
        devolver = dias[numero - 1]

def calcualar_factorial(num):
    if  num < 0:
        devolver = 0
    elif num == 0:
        devolver = 1
    else:
        inicio = 1
        devolver = 1
        while inicio <= num:
            devolver *= inicio
            inicio += 1
    return devolver

def calcualar_suma_valor_n(num):
    inicio = 1
    numero_sumados = 0
    while inicio <= num:
        numero_sumados += inicio
        inicio +=1
    return numero_sumados

def delvolver_resta_de_puntos(pun1, pun2):
    indice = 0
    suma_puntos = []
    while indice < len(pun1):
        valor = pun2[indice] - pun1[indice]
        suma_puntos.append(valor)
        indice += 1
    return tuple(suma_puntos)

def devolver_pendiente_por_2_puntos(pun1, pun2):
    resta_puntos_especial = delvolver_resta_de_puntos(pun1,pun2)
    x = resta_puntos_especial[0]
    y = resta_puntos_especial[1]

    if x == 0:
        devolver = "Pendiente infinita cuidado"
    else:
        devolver = y / x
    return devolver

# todo numero primo es no primo si son negativos, es primo si es 2, no es primo si es divisible por 2 entonces que necesidad hay de evaluar los pares??
def es_primo(num):
    if num <= 1:
        devolver = False
    elif num == 2:
        devolver = True
    elif num %= 2 == 0:
        devolver = False
    else:
        contador = 3
        devolver = True
        while contador < num:
            if num % contador == 0:
                devolver = False
            contador += 2
    return devolver

def devolver_divisor_max_numero(num):
    valor = num - 1
    while num % valor != 0 and valor > 1:
        valor -= 1
    return valor
def devolver_divisor_min_numero (num):
    valor = 2
    while num % valor != 0 and valor < num:
        valor += 1
    return valor

def devolver_max_comun_divisor_entre_2_numeros(num1, num2):
    condicion = False
    divisor_2 = 1
    divisor_mayor_1 = 1
    devolver = 1
    if num1 > num2:
        while not condicion and divisor_mayor_1 != devolver_divisor_min_numero(num1):
            divisor_mayor_1 = devolver_divisor_max_numero(num1)
            while divisor_mayor_1 != divisor_2 and divisor_2 != devolver_divisor_min_numero(num2):
                divisor_2 = devolver_divisor_max_numero(num2)
            if divisor_mayor_1 == divisor_2:
                condicion = True
                devolver = divisor_mayor_1
    else:
        while not condicion and divisor_2 != devolver_divisor_min_numero(num2):
            divisor_2 = devolver_divisor_max_numero(num1)
            while divisor_2 != divisor_mayor_1 and divisor_mayor_1 != devolver_divisor_min_numero(num1):
                divisor_mayor_1 = devolver_divisor_max_numero(num1)
            if divisor_2 == divisor_mayor_1:
                condicion = True
                devolver = divisor_2
    return devolver












