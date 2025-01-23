# X94960
# How old is my neighbor’s Chihuahua?

chihuahua_age = int(input())
chihuahua_name = input() 

# Cálculo de los años humanos
if chihuahua_age <= 2:
    human_age = chihuahua_age * 10
else:
    human_age = 20 + (chihuahua_age - 2) * 4


print(f"{chihuahua_name} is {human_age} human years old")
