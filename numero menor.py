# Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. 
# Considerar el caso en que ambos números son iguales.

from typing import NoReturn


numero_uno=int(input())
numero_dos=int(input())
if numero_uno>numero_dos:
    print("el primer numero ingresado es Mayor "+numero_uno)
elif numero_uno<numero_dos:
    print("el segundo numero es Mayor "+numero_dos)
else:
   print("los numeros son iguales ")
