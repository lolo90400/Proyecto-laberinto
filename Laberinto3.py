from readchar import readkey
import os 

numero = 0
def delete():
    os.system('cls' if os.name=='nt' else 'clear')

while numero <51:
    delete()
    print(numero)
    llave = readkey()
    
    if llave == "n":
        numero += 1 
    else:
        break
        




