"""
Escribir un programa que pregunte el nombre del
usuario en la consola y después de que el usuario 
lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el 
número de letras que tienen el nombre.
"""

#Ejercicio 3 upper/len

nombre_usurio = input("Ingrese su nombre de usuario")
print(nombre_usurio.upper() + " contiene " + str(len(nombre_usurio)) + " letras ")