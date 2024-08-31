"""
Escribir un programa que pregunte al usuario 
la fecha de su nacimiento en formato dd/mm/aaaa 
y muestra por pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione 
cuando el día o el mes se introduzcan con un solo carácter.
"""

#Ejercicio 9

fecha_de_nacimiento = input("Coloque su fecha de nacimiento en el siguiente formato dd/mm/aaaa: ")
dia = fecha_de_nacimiento[:fecha_de_nacimiento.find('/')]
mesaño = fecha_de_nacimiento[fecha_de_nacimiento.find('/') + 1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/') + 1:]
print('Dia', dia)
print('Mes', mes)
print('Año', año)