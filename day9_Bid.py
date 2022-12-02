# This Ceaser Ciper is done with Ascii value and  using range
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

print('Welcome to the secret auction program')

user = {} 
cont = 'y'
while cont=='y':
    name = input("What is your name?: ")
    bid = int(input("What\'s your bid?: $"))
    user[name] = bid
    cont = input("Type y to continue and no to finish\n")
    os.system('cls')
win = max(user,key=user.get)
print("The winner is",win,"with a bid of $"+str(user[win]))