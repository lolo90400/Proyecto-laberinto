from readchar import readkey, key

print("presionar cualquier tecla, para salir del bucle presiona la tecla 'up'")

while True:
    tecla=readkey()
    if tecla == key.UP:
        print("Tecla UP  finalizando el programa")
    else:
        print(f"Presionaste la tecla {tecla}")


