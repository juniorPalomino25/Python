import math

print("\t\tMENU")
print("1. EXPRESION MATEMATICA: a^3*(b^2-2ac)/(2b)")
print("2. EXPRESION LOGICA: ((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b) ")
print("")
opc = int(input("DIGITE UNA OPCION (1) o (2): \n"))

if opc==1:
    a = int(input("Digite un valor para a: "))
    b = int(input("Digite un valor para b: "))
    c = int(input("Digite un valor para c: "))

    resultado1 = pow(a, 3) * (pow(b, 2) - 2 * a * c) / (2 * b)
    print("el resultado de la expresion 1 es: ", resultado1)
else:
    a = int(input("Digite un valor para a: "))
    b = int(input("Digite un valor para b: "))
    resultado2 = ((3 + 5 * 8) < 3 and ((-6 / 3 * 4) + 2 < 2)) or (a > b)
    print("el resultado de la expresion 2 es: ", resultado2)

