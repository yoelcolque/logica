# ABRIR DOCUMENTO POR UNA LINEA Y CIERRO
# FUNCION PARA SUMAR EL ULTIMO ELEMENTO DE FORMA INCREMENTAL
# FUNCION PARA IMPRIMIR
# FUNCION PARA GUARDAR


#HAY UNA CONTASTE MAX_DIA SIMPLICA MUCHO CODIGO, ¿SE TERMINO EL ARCHIVO?
"""
* función leer archivo - lee una línea del archivo
*
* pre: f es un archivo abierto con líneas con formato válido
* post: devuelve la línea como una lista de 3 valores
*       dia, cliente, valor
*       si llegó al fin de archivo devuelve MAX_REG
"""

def leer(archivo):
    linea = archivo.readline()
    if not linea: #SI LINEA ESTA VACIA
        linea = MAX_REG
    else:
        linea = linea.rstrip()
    return linea.split(',')
"""
    * funcion corte de control
    *
    * pre: recibe un archivo abierto valido
    *
    * post: realiza el corte de control x pantalla
"""

def corte_control(f):
    # Leo la primera línea
    registro = leer(f)
    suma_total = 0

    while registro[0] < MAX_DIA:
        imprimir("Total del día", registro[0])
        suma_dia, registro = total_dia(registro, f)
        # Acá va el corte de control
        imprimir("Acumulado", suma_dia, True)
        suma_total += suma_dia

    imprimir("\n ==== Acumulado total =", suma_total)

def total_dia(registro, f):
    dia, valor = dia_valor(registro)
    dia_actual = dia
    acum_dia = 0

    while dia == dia_actual and dia < MAX_DIA:
        acum_dia += valor
        registro = leer(f)
        dia, valor = dia_valor(registro)

    return acum_dia, registro

"""
    * funcion imprimir
    *
    *
    *
"""


def main():
    print("------------------------------------------")
