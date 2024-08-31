"""
Escribir un programa que pregunte el nombre del usuario en 
la consola y un número entero e imprima por pantalla en líneas 
distintas el nombre del usuario tantas veces como el número introducido
"""
#Ejecicio 1 

nombre_de_usuario = input("Ingrese su nombre")
numero_entero = int(input("Ingrese numero entero"))
print((nombre_de_usuario + "\n") * int(numero_entero))
