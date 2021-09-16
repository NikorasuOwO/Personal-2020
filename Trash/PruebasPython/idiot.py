import random

def idiot(s):
    if s == "":
        return ""
    
    a = random.random()

    if a < 0.7:
        return s[0].upper() + str(idiot(s[1:]))
    else:
        return s[0] + str(idiot(s[1:]))



frase = idiot(input("Escribe una frase: "))
print(frase)