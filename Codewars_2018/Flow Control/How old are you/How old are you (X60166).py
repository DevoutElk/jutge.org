# X60166
# How old are you?
# 'https://jutge.org/problems/X60166_en'

revolution_in_earth = {"Mercury":88,"Venus":225,"Mars":687,"Jupiter":4333,"Saturn":10759,"Uranus":30689,"Neptune":60182,"Earth":365}

earth_age = int(input())
planet_name = input()

result = int((int(revolution_in_earth[planet_name]) / revolution_in_earth["Earth"])*earth_age)

print(result)