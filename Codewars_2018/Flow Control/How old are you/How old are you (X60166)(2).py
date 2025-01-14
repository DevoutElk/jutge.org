# X60166
# How old are you?
# 'https://jutge.org/problems/X60166_en'
# Definir el diccionario con la tabla de períodos de revolución en días de cada planeta
planet_revolution_periods = {
    "Mercury": 88,
    "Venus": 225,
    "Earth": 365,
    "Mars": 687,
    "Jupiter": 4333,
    "Saturn": 10759,
    "Uranus": 30689,
    "Neptune": 60182
}

# Obtener la edad y el nombre del planeta desde la entrada del usuario
age_in_planet = int(input())
planet_name = input()

# Calcular la equivalencia en años terrestres
earth_age = age_in_planet * planet_revolution_periods[planet_name] / planet_revolution_periods["Earth"]

# Imprimir la edad en años terrestres como un entero
print(int(earth_age))
