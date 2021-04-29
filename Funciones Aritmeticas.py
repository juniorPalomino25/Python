import math
import os
import time

#PARA LIMPIAR PANTALLA
if os.name == "posix":
   var = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
   var = "cls"

band = 's'

while(band == 's'):
    print("\t\t\tMENU")
    print("1. EXPRESION MATEMATICA: a^3*(b^2-2ac)/(2b)")
    print("2. EXPRESION LOGICA: ((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b) ")
    print("3. INTERCAMBIAR VALOR ")
    print("4. AREA Y LONGITUD DE UNA CIRCUNFERENCIA ")
    print("5. PROBLEMA DE DESCUENTO ")

    opc = int(input("DIGITE UNA OPCION: \n"))

    if opc==1:
        a = float(input("Digite un valor para a: "))
        b = float(input("Digite un valor para b: "))
        c = float(input("Digite un valor para c: "))

        resultado1 = pow(a, 3) * (pow(b, 2) - 2 * a * c) / (2 * b)
        print("el resultado de la expresion 1 es: ", resultado1)
    elif opc==2:
        a = float(input("Digite un valor para a: "))
        b = float(input("Digite un valor para b: "))
        resultado2 = ((3 + 5 * 8) < 3 and ((-6 / 3 * 4) + 2 < 2)) or (a > b)
        print("el resultado de la expresion 2 es: ", resultado2)

    elif opc==3:
        a = float(input("Digite un valor para a: "))
        b = float(input("Digite un valor para b: "))
        aux = a
        a = b
        b = aux
        print("el nuevo valor de a es: ", a)
        print("el nuevo valor de b es: ", b)
    elif opc==4:
        r = float(input("Digite un valor para el radio r: "))
        area = math.pi * pow(r,2)
        lomgitud = 2 * math.pi * r
        print("el area es: ", area)
        print("la longitud es: ", lomgitud)
    else:
        precio = float(input("Digite el precio: "))
        descuento = 0.15*precio
        pago = precio - descuento
        print("el pago total es: $", pago)

    band = input("desea continuar si 's' / no 'n' : ")
