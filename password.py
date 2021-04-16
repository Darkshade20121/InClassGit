import random
import string

def password(num):
    password = []
    letters = string.ascii_letters

    for i in range (0,num):
        password.append(random.choice(letters))
        
    for i in range(len(password)):
        print(password[i],end='')
        

password(5)
    
