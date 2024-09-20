import random

alph_l = "abcdefghijklmnopqrstuvwxyz"
alph_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
symb = "`~!@#$%^&*()-_=+[{]}\|<,.>/?"

all = alph_l + alph_u + num + symb
length = 16
password = "".join(random.sample(all,length))
print("\n")
print(password) #creates a 16 letter password
print("\n")
