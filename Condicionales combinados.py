#Condicionales Combinados
'''
edad = int(input("digite su edad: "))

if edad >= 18:
    print("es mayor de edad")
else:
    print("no es mayor de edad")
'''
# problema numeros pares
'''
n1 = int(input("digite primer numero: "))
n2 = int(input("digite segundo numero: "))
aux1= n1 % 2
aux2= n2 % 2
if aux1 == 0 and aux2 ==0:
    print(n1," y ", n2 ," son pares")
elif aux1 !=0 and aux2 == 0:
    print(n2, " es par")
elif aux1 ==0 and aux2 != 0:
    print (n1, "es par")
else:
    print ("ambos son impares")

# digitar 3 numero y encontrar el numero mayor
n1 = int(input("digite primer numero: "))
n2 = int(input("digite segundo numero: "))
n3 = int(input("digite tercer numero: "))
aux = n1
if n2 > aux:
    aux = n2
if n3 > aux:
    aux = n3
print("el numero mayor es: ", aux)
'''

saldo = 1000
print("*********MENU DE OPCIONES******")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero en la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")

opcion = int(input("digite una opcion: "))
print()
while opcion != 4:
    if(opcion==1):
        ingreso=int(input("digite la cantidad de dinero a ingresar: "))
        saldo += ingreso
    elif(opcion==2):
        retiro=int(input("digite la cantidad de dinero a retirar:"))
        if(retiro>saldo):
            print("A excedido el monto a retirar")
        else:
            saldo -= retiro
    else:
        print(saldo)
    opcion = int(input("digite una opcion: "))
print("gracias por su visita")
