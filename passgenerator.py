import random

a=int(input(4"Ile znaków ma liczyć twoje hasło?"))
b=("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
c=" "
for i in range(a):
    c+= random.choice(b)
print(c)
