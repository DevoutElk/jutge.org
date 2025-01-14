#  Which GPU should I buy?
#  X69142
# 'https://jutge.org/problems/X69142_en'


n = 0
gpu_freq = int(input())
while (game_freq := int(input())) != 0:
    if gpu_freq >= game_freq:
        n += 1
print(n)
