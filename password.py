import random

def password(num):
    password = []
    for i in range (0,num):
        password.append(random.choice(chars))
        
    for i in range(len(password)):
        print(password[i])
    
