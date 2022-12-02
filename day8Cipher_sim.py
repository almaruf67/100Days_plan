# This Ceaser Ciper is done with lower alphabet  and  using range
print(
    """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
)

alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def enco():
    message = input("Type your message:\n")
    message = message.lower()
    shift = int(input("Type the shift number\n"))
    en_mes = ''
    for i in range(0,len(message)):
        for j in range(0,26):
            if message[i]==alp[j] and 25<j+shift:
                en_mes+=alp[j+shift-25]
                break
                
            elif message[i]==alp[j] :
                en_mes+=alp[j+shift]
                break
            
        if i+1 !=len(en_mes):
            en_mes+=message[i]
        
    print(en_mes)

def deco():
    message = input("Type your message:\n")
    message = message.lower()
    shift = int(input("Type the shift number\n"))
    en_mes = ''
    for i in range(0,len(message)):
        for j in range(0,26):
            if message[i]==alp[j] and 0>j-shift:
                en_mes+=alp[j-shift-1]
                break
                
            elif message[i]==alp[j] :
                en_mes+=alp[j-shift]
                break
            
            
        if i+1 !=len(en_mes):
            en_mes+=message[i]
        
    print(en_mes)

cont = 'yes'

while(cont=='yes'):
    fun = input("Type \'encode\' to encrypt, type \'decode\' to decrypt\n")
    if fun=="encode":
        enco()
    elif fun=="decode":
        deco()
    else:
        print("Ïnvalid")
    cont = input("Type \'yes\' if you want to go again. otherwise type \'no\'.\n")


