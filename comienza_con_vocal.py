"""
Comienza con vocal
"""

# Declaraciones
VOCALES = "aeiouáéíóúü"

# Entradas
palabra = input("Escribe una palabra: ")

# Proceso
if palabra[0].lower() in VOCALES:
    comienza = "comienza"
else:
    comienza = "no comienza"
salida = f"'{palabra}' {comienza} con vocal"

# Salidas
print(salida)
