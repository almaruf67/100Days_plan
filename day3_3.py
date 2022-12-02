from itertools import count


print("Welcome to love calculator")
name1 = input("Enter your name :")
name2 = input("Enter your partners name :")
name1 = name1.lower()
name2 = name2.lower()

tr = name1.count('t')+ name1.count('r') + name1.count('u') + name1.count('e')+ name2.count('t')+ name2.count('r') + name2.count('u') + name2.count('e')
lv = name1.count('l')+ name1.count('o') + name1.count('v') + name1.count('e')+ name2.count('l')+ name2.count('o') + name2.count('v') + name2.count('e')
print(f'Your love score is {tr}{lv}%')
