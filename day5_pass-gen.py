import random
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0','1','2','3','4','5','6','7','8','9']
sym = ['~','!','@','#','$','%','^','&','*','(',')','-']

print(sym)

print("Welcome to the password Generator!")

ch = int(input("How many letters would you like in your password "))
nu = int(input("How many numbers would you like "))
sy = int(input("How many symbols would you like "))

print(ch//2)

gpass = []

for i in range(ch//2):
    gpass.append(random.choice(char))
for i in range(nu//2):
    gpass.append(random.choice(num))
for i in range(sy//2):
    gpass.append(random.choice(sym))   

for i in range(ch-ch//2):
    gpass.append(random.choice(char))
for i in range(nu-nu//2):
    gpass.append(random.choice(num))
for i in range(sy-sy//2):
    gpass.append(random.choice(sym))

print("You password is :",end=' ')
for i in gpass:
    print(i,end='')
random.shuffle(gpass)
print("\nYour new password is :",end=' ')
for i in gpass:
    print(i,end='')