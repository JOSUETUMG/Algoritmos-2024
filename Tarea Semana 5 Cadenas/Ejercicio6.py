"""
Escribir un programa que pida al usuario 
que introduzca una frase en la consola y una vocal, 
y después muestre por pantalla la misma frase pero con la 
vocal introducida en mayúscula.
"""

#Ejercicio 6 Replace

frase_a_ingresar = input("Intruduce tu frase: ")
vocal_ingresada = input("Ingresa vocal en minuscula:  ")
print(frase_a_ingresar.replace(vocal_ingresada, vocal_ingresada.upper()))