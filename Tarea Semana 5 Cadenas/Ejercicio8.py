"""
Escribir un programa que pregunte 
por consola el precio de un producto 
en euros con dos decimales y muestre por 
pantalla el número de euros y el número de 
céntimos del precio introducido.
"""

#Ejercicio 8 Find

precio_producto = input("Ingrese el precio del producto en dos decimales")
print(precio_producto[:precio_producto.find('.')], 'euros y', precio_producto[precio_producto.find('.') + 1:], 'centimos.')