"""
Escribir un programa que pregunte 
por consola por los productos de una 
cesta de la compra, separados por comas, 
y muestre por pantalla cada uno de los productos 
en una línea distinta.
"""

#Ejercicio 10 Replace

cesta_de_compras = input("Ingreser los productos en la cesta de compra y separelos por comas: ")
print(cesta_de_compras.replace(',', '\n'))