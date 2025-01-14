pen = int(input()) # Introducir pen de x GB
song = 11 # Tamaño de una canción en MB

pen2 = pen*2**10 # Convertir pen a MB

resultado = (pen2 // song) # Dividir pen2 entre song

print(resultado,"songs") # Total de canciones que se pueden almacenar en el pen