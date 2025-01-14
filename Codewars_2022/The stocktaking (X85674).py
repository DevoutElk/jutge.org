# The stocktaking
# X85674
# 'https://jutge.org/problems/X85674_en/'

cantidad_productos = int(input()) 
cajas = int(input())
restantes = int(input())


if (cantidad_productos % cajas == restantes) :
    print(f"CORRECT, the capacity of each box is {cantidad_productos//cajas}")
else:
    print("INCORRECT")

 