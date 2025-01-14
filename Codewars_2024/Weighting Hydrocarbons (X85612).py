# Weighting Hydrocarbons
# X85612
num_C_atoms = int(input())

num_H_atoms = num_C_atoms * 2 + 2 # Numreo de atomos de hidrogeno


atomic_weight = (num_C_atoms * 12 + num_H_atoms) # Peso atomico


print(f"The atomic mass of C{num_C_atoms}H{num_H_atoms} is {atomic_weight}")
