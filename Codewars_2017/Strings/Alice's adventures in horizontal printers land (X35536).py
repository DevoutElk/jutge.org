# X35536
# Alice's adventures in horizontal printers land

resultado = [] # Debemos guardar los valores en una lista para poder utilizarlos más tarde.

while True:
    numeros = input()   # Bucle de inputs

    if numeros == "#":   # Detiene el bucle si el input es un "#"
        break
    
    resultado.append(numeros[::-1]) # Añade los inputs invertidos a la lista.

for lista in resultado: # Muestra el contenido por linea
    print(lista)