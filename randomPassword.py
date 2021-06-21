import random 

passlen = int(input('enter the length of password: '))
s = "abcdefghijklmnopqrstuvxwyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()?"
p = "".join(random.sample(s,passlen))
print(p)