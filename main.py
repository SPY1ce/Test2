import random
password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
a = int(input("Какой длины хотите сделать пароль: "))
b = ""
for c in range (a):
    b += random.choice(password)
print(b)