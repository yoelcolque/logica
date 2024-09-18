def evaluar_valor_impar(valor): 
    return valor%2 != 0

def delvolver_nombre_mes_por_numero(numero):
    meses = ("ene","feb","marz","abri","may","jun","jul","ago","sep","oct","nob","dic")
    if numero < 1 or numero > 12:
        devolver = "Mes INvalido"
    else:
        devolver = meses[numero-1]
    return devolver

def calcualr_factorial(numero):
    if numero < 0:
        devolver = 0
    elif numero == 0:
        devolver = 1
    else:
        devolver = 1
        for e in range(2,numero+1):
            devolver *= e    
    return devolver

def devolver_numero_mayor_0(numero):
    while numero < 0:
        print("ERROR: El valor a ingresar debe ser mayor a 0")
        numero = int(input("INGRESE UN NUEMRO MAOY A 0"))
    return numero    

def calcular_potencia(a,b):
    for e in range(b):
        devolver *= a
    return devolver

def calcular_exp_negativo(a,b):
    b = abs(b)
    devolver = 1 / calcular_potencia(a,b)
    return devolver

def devolver_longitud_circle(radio):
    return radio * 2 * 3.14
def devolver_area_circle(radio):
    return radio ** 2 * 3.14
def devolver_equivalencia_cm_pul(cm):
    return cm * 0.393701
def devolver_perimetro_area_rectangulo(base, altura):
    perimetro = base *2 + altura *2
    area = base * altura
    return perimetro,area
def devolver_equicalencia_fatren_celcius(faren):
    return (f - 32)/1.8
def devolver_distancia_recorida_por_velocidad_tiempo(velocidad,tiempo):
    return velocidad * tiempo
def devolver_equivalencia_en_dia_hora_min_segun(segundos):
    minutos = segundos /60
    horas = (segundos / 60)/60     
    dias = ((segundos/60)/60)/24
    return dias, horas, minutos, segundos
def es_mayor(num1, num2):
    return num1 > num2
def es_impar(numero):
    return numero%2 != 0
def es_multiplo_de(num1, num2):
    return num1 % num2 ==0
