#X32365
#  Does my car fit in that parking slot?

space_needed = input()
space_found = input()

# Try
width_needed,height_needed = space_needed.split(' ')
width_found,height_found = space_found.split(' ')



# Main Ancho del coche igual o menor al ancho encontrado y el largo del coche igual o menor que el largo encontrado o el ancho del coche es menor o igual al largo encontrado y el largo del coche es igual o menor que el ancho encontrado

if int(width_needed) <= int(width_found) and int(height_needed) <= int(width_found) or int(width_needed) <= int(height_found) and int(height_needed) <= int(width_found):
    print("yes")
else:
    print("no")
