# X45256
# Internet shoe shopping


genero = str(input())
talla = int(input())

if genero == "M":
    if talla <44:
        resultado = talla - 34.5
    else:
        resultado = talla - 35

elif genero == "L":
    if talla <40:
        resultado = talla - 31.5
    else:
        resultado = talla - 32

print(f"{resultado:.1f}")